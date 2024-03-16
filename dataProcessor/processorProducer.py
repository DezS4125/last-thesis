from kafka import KafkaProducer
import os
import time


def setup_producer():
    try:
        producer = KafkaProducer(bootstrap_servers="192.168.1.241:9092")
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