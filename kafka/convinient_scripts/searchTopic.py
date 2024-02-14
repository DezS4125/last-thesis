from confluent_kafka.admin import AdminClient

# Replace with your Kafka broker's IP and port
KAFKA_BROKER = '192.168.1.241:9092'

def list_topics_with_prefix(prefix):
    admin_client = AdminClient({'bootstrap.servers': KAFKA_BROKER})
    topics = admin_client.list_topics().topics
    return [topic for topic in topics.keys() if topic.startswith(prefix)]

print("Listing all topics in Kafka cluster starting with 'video-'...")
print(list_topics_with_prefix("video"))