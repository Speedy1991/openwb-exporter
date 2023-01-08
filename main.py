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
        topic_length = len(topic.split('/'))
        if topic_length == 3:
            _unused, metric, measurement = topic.split('/')
            g = Gauge(name=topic_name, documentation=description, labelnames=['metric', 'topic'])
            g.labels(metric=metric, topic=topic)
        elif topic_length == 4:
            _unused, metric, device_id, measurement = topic.split('/')
            g = Gauge(name=topic_name, documentation=description, labelnames=['metric', 'device_id', 'topic'])
            g.labels(metric=metric, device_id=device_id, topic=topic)
        else:
            raise Exception(f"Unknown topic length: {topic}")
        collectors[topic] = g


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    for topic, gauge in collectors.items():
        client.subscribe(topic)
        print("Subscribed to", topic)


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    collector = collectors.get(msg.topic)
    collector.set(msg.payload)
    collector.set_to_current_time()


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
