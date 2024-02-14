from confluent_kafka.admin import AdminClient, NewTopic

# Replace with your Kafka broker's IP and port
KAFKA_BROKER = '192.168.1.241:9092'

def create_topic(base_name):
    admin_client = AdminClient({'bootstrap.servers': KAFKA_BROKER})
    existing_topics = admin_client.list_topics().topics

    i = 1
    while True:
        topic_name = f"{base_name}-{i}"
        if topic_name not in existing_topics:
            break
        i += 1

    topic = NewTopic(topic_name, num_partitions=1, replication_factor=1)
    admin_client.create_topics([topic])

    print(f"Created new topic: {topic_name}")

create_topic("video")