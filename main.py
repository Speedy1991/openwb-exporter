import os

import paho.mqtt.client as mqtt
from prometheus_client import Gauge, start_http_server
import prometheus_client

from config import topics

collectors = dict()


def setup_collectors():
    prometheus_client.REGISTRY.unregister(prometheus_client.GC_COLLECTOR)
    prometheus_client.REGISTRY.unregister(prometheus_client.PLATFORM_COLLECTOR)
    prometheus_client.REGISTRY.unregister(prometheus_client.PROCESS_COLLECTOR)

    for topic, description in topics:
        topic_name = topic.replace('/', '_').replace('openWB_', '').replace('%', 'percentage_')
        collectors[topic] = Gauge(name=topic_name, documentation=description, labelnames=["topic", "device", "measurement"])

    # Special stuff
    collectors['special/autark/daily'] = Gauge('special_autark_daily', documentation='Autarkiegrad in Prozent (Daily)', labelnames=["device"])
    collectors['special/autark/live'] = Gauge('special_autark_live', documentation='Autarkiegrad in Prozent (Live)', labelnames=["device"])
    collectors['invert/pv/W'] = Gauge('invert_pv_W', documentation='Invertierte PV W', labelnames=["device"])
    collectors['special/total_kwh/daily'] = Gauge('special_total_kwh_daily', documentation='Kompletter täglicher Verbrauch in KW', labelnames=["device"])
    collectors['special/total_w/live'] = Gauge('special_total_kwh_live', documentation='Aktueller Verbrauch in W', labelnames=["device"])


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    for topic, gauge in collectors.items():
        client.subscribe(topic)
        print("Subscribed to", topic)


def _topic_to_tuple(topic):
    device = topic.split('/')[1]
    if device == 'global':
        device = 'openWB'
    measurement = topic.split('/')[-1]
    return topic, device, measurement


def _get_current_value(topic):
    collector = collectors.get(topic)
    return collector.labels(*_topic_to_tuple(topic))._value.get()


def on_message(client, userdata, msg):
    print('Message', msg.topic + " " + msg.payload.decode('utf-8'))
    collector = collectors[msg.topic]
    value = msg.payload.decode('utf-8')
    collector.labels(*_topic_to_tuple(msg.topic)).set(value)

    daily_all_charge_points_kwh = _get_current_value('openWB/global/DailyYieldAllChargePointsKwh')
    daily_hausverbrauch_kwh = _get_current_value('openWB/global/DailyYieldHausverbrauchKwh')
    daily_total_kwh = daily_hausverbrauch_kwh + daily_all_charge_points_kwh
    daily_evu_import_kwh = _get_current_value('openWB/evu/DailyYieldImportKwh')

    pv_w = abs(_get_current_value('openWB/pv/W'))
    current_w = _get_current_value('openWB/evu/W')

    if current_w < 0:
        collectors['special/autark/live'].labels('openWB').set(1)
    elif current_w:
        collectors['special/autark/live'].labels('openWB').set(pv_w / (pv_w + current_w))

    collectors['invert/pv/W'].labels('openWB').set(pv_w)
    collectors['special/total_kwh/daily'].labels('openWB').set(daily_total_kwh)

    house_w_live = _get_current_value('openWB/global/WHouseConsumption')
    lp_w_live = _get_current_value('openWB/global/WAllChargePoints')

    collectors['special/total_w/live'].labels('openWB').set(house_w_live + lp_w_live)

    if daily_total_kwh and daily_evu_import_kwh:
        collectors['special/autark/daily'].labels('openWB').set((daily_total_kwh - daily_evu_import_kwh) / daily_total_kwh)


def start():
    open_wb = os.environ.get('OPEN_WB', None)
    if not open_wb:
        print('OPEN_WB environment must be set. E.g. OPEN_WB=openwb.fritz.box python main.py')
        exit(1)
    setup_collectors()

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    # Try to connect before we serve the metrics
    client.connect(open_wb, 1883, 60)
    start_http_server(5555)

    client.loop_forever()


if __name__ == '__main__':
    start()
