import os

import paho.mqtt.client as mqtt
from prometheus_client import Gauge, start_http_server
import prometheus_client

from config import topics

connectors = dict()
for topic, description in topics:
    topic_name = topic.replace('/', '_').replace('openWB_', '')
    topic_length = len(topic.split('/'))
    device_id = None
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
    connectors[topic] = g


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    for topic, gauge in connectors.items():
        client.subscribe(topic)
        print("Subscribed to", topic)


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    connector = connectors.get(msg.topic)
    connector.set(msg.payload)


if __name__ == '__main__':
    open_wb = os.environ['OPEN_WB']
    prometheus_client.REGISTRY.unregister(prometheus_client.GC_COLLECTOR)
    prometheus_client.REGISTRY.unregister(prometheus_client.PLATFORM_COLLECTOR)
    prometheus_client.REGISTRY.unregister(prometheus_client.PROCESS_COLLECTOR)

    start_http_server(5555)
    c = mqtt.Client()
    c.on_connect = on_connect
    c.on_message = on_message
    c.connect(open_wb, 1883, 60)
    c.loop_forever()
