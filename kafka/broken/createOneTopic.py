from confluent_kafka.admin import AdminClient, NewTopic

def create_kafka_topic(broker, topic_name):
    admin_client = AdminClient({'bootstrap.servers': broker})

    topic = NewTopic(
        topic_name,
        num_partitions=1,
        replication_factor=1
    )

    admin_client.create_topics([topic])

if __name__ == "__main__":
    create_kafka_topic('192.168.1.241:9092', 'my_topic')
