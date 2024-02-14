from kafka import KafkaConsumer

consumer = KafkaConsumer('my-topic', bootstrap_servers='192.168.1.241:9092,192.168.1.241:9093,192.168.1.241:9094')

for message in consumer:
    print (message)
