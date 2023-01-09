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
        collectors[topic] = Gauge(name=topic_name, documentation=description, labelnames=["topic", "metric", "measurement"])

    collectors['special/autark'] = Gauge('special_autark', documentation='Autarkiegrad in Prozent')


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    for topic, gauge in collectors.items():
        client.subscribe(topic)
        print("Subscribed to", topic)


def _topic_to_tuple(topic):
    return topic, topic.split('/')[1], topic.split('/')[-1]


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
    if not all([daily_total_kwh, daily_evu_import_kwh]):
        return
    collectors['special/autark'].set((daily_total_kwh - daily_evu_import_kwh) / daily_total_kwh)


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
