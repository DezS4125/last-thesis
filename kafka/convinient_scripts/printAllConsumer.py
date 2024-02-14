from kafka import KafkaConsumer

# Create a Kafka consumer
consumer = KafkaConsumer(
    'my-topic',  # replace with your topic name
    bootstrap_servers='192.168.1.241:9092,192.168.1.241:9093,192.168.1.241:9094',
    auto_offset_reset='earliest',  # start at earliest topic
    # enable_auto_commit=True,  # commit offsets for you
)
# Print all messages from the topic
for message in consumer:
    print(message.value)
