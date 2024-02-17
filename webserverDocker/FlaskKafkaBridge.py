import os
import time
from flask import Flask, request
from kafka import KafkaProducer

BOOTSTRAP_SERVERS = os.environ.get('BOOTSTRAP_SERVERS', '192.168.1.241:9091,192.168.1.241:9092,192.168.1.241:9093').split(',')

def setup_producer():
    try:
        producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)
        return producer
    except Exception as e:
        if e == 'NoBrokersAvailable':
            print('waiting for brokers to become available')
        return 'not-ready'

print('setting up producer, checking if brokers are available')
producer='not-ready'

while producer == 'not-ready':
    print('brokers not available yet')
    time.sleep(5)
    producer = setup_producer()

print('brokers are available and ready to produce messages')

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_frame():
    frame_bytes = request.data
    kafka_topic = request.headers.get('kafka-topic')
    print("sending to kafka topic: "+kafka_topic)
    producer.send(kafka_topic, frame_bytes)
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
