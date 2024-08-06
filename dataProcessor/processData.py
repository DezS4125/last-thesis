 
from kafka import KafkaConsumer, KafkaProducer
import time
import json
topics = ['video-stream-1', 'video-stream-2', 'video-stream-3']
# topics = ['video-stream-1']

def setup_consumer_producer():
    try:
        consumer = KafkaConsumer(*topics, bootstrap_servers='192.168.1.241:9092')
        producer = KafkaProducer(bootstrap_servers="192.168.1.241:9092",value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        return consumer, producer
    except Exception as e:
        if e == 'NoBrokersAvailable':
            print('waiting for brokers to become available')
        return 'not-ready','not-ready'

print('setting up producer, checking if brokers are available')
consumer='not-ready'
producer='not-ready'

while producer == 'not-ready':
    print('brokers not available yet')
    time.sleep(5)
    consumer, producer = setup_consumer_producer()

print('brokers are available and ready to consume and produce messages')

for message in consumer:
    print(f'Received message from topic: {message.topic}')
    data = {
        'field1': 'test '+message.topic,
        'field2': 'string2',
        'field3': 1,
        'field4': 2
    }
    outputTopic="output-"+message.topic
    producer.send(outputTopic, data)
    



