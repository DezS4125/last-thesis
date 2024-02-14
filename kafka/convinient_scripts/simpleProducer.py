from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='192.168.1.241:9092,192.168.1.241:9093,192.168.1.241:9094')

some_data_source = ['Hello, world!', 'Kafka is great', 'Python is my favorite language', 'Have a nice day!', 'This is the last message']

for data in some_data_source:
    producer.send('my-topic', data.encode('utf-8'))
    
