from confluent_kafka.admin import AdminClient

def list_kafka_topics(broker):
    admin_client = AdminClient({'bootstrap.servers': broker})

    cluster_metadata = admin_client.list_topics(timeout=10)
    topics = cluster_metadata.topics

    for topic in topics.values():
        if not topic.topic.startswith('_'):
            print(topic.topic)

if __name__ == "__main__":
    list_kafka_topics('192.168.1.241:9092')
