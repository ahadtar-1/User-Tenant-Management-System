import json
from kafka import KafkaConsumer
import asyncio
import os

TOPIC_NAME = 'data_topic'

KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')
#KAFKA_CONSUMER_GROUP = os.getenv('KAFKA_CONSUMER_GROUP', 'group')
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9094')

consumer = KafkaConsumer(
    TOPIC_NAME,
    auto_offset_reset='earliest', # where to start reading the messages at
    group_id='event-collector-group-1', # consumer group id
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')) # we deserialize our data from json
)

#TOPIC_NAME = 'data_topic'


def consume_events():
    for m in consumer:
        # any custom logic you need
        #print(m.value)
        return m.value

#if __name__ == '__main__':
    #consume_events()