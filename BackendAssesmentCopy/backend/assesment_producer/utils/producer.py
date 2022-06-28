from datetime import datetime
import json
from json import dumps
import asyncio
from kafka import KafkaProducer
import os
from random import randint
#import random
#import time
#import uuid

KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

producer = KafkaProducer(
   value_serializer=lambda msg: json.dumps(msg).encode('utf-8'), # we serialize our data to json for efficent transfer
   bootstrap_servers='kafkatwo:9092')

TOPIC_NAME = 'data_topic'

def produce_event():
    final_msg = "Process done"
    return final_msg

def send_events(data):
    #data = produce_event()
    print(producer.bootstrap_connected(),flush=True)
    producer.send(TOPIC_NAME, value=data)
