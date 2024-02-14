from confluent_kafka import Consumer

# Replace with your Kafka broker's IP and port
KAFKA_BROKER = '192.168.1.241:9092,192.168.1.241:9093,192.168.1.241:9094'

def print_broker_info():
    consumer = Consumer({'bootstrap.servers': KAFKA_BROKER, 'group.id': 'mygroup'})
    cluster_metadata = consumer.list_topics(timeout=10)
    for broker_id, broker in cluster_metadata.brokers.items():
        print(f"Broker ID: {broker_id}")
        print(f"Broker host: {broker.host}")
        print(f"Broker port: {broker.port}")

print_broker_info()
