from confluent_kafka import Producer

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

p = Producer({'bootstrap.servers': '192.168.1.241:9092'})

some_data_source = ['Hello, world!', 'Kafka is great', 'Python is my favorite language', 'Have a nice day!', 'This is the last message']

for data in some_data_source:
    p.produce('mytopic', data.encode('utf-8'), callback=delivery_report)

p.flush()