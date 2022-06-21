import json
from sys import api_version
from kafka import KafkaConsumer
from kafka import KafkaProducer
import asyncio
import os

TOPIC_NAME = "data_topic"

# KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')
# KAFKA_CONSUMER_GROUP = os.getenv('KAFKA_CONSUMER_GROUP', 'group')
# KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

# producer = KafkaProducer(
# value_serializer=lambda msg: json.dumps(msg).encode('utf-8'), # we serialize our data to json for efficent transfer
# bootstrap_servers='localhost:9092', api_version=(0,10))


consumer = KafkaConsumer(
    TOPIC_NAME, auto_offset_reset="earliest", bootstrap_servers="kafkatwo:9092"
)


def consume_events():
    for m in consumer:
        print("Value consumed", m, flush=True)


# if __name__ == '__main__':
# consume_events()
