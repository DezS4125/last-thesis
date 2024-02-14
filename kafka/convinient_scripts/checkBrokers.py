from kazoo.client import KazooClient

def get_broker_count(zookeeper_servers):
    # Create a KazooClient instance
    zk = KazooClient(hosts=zookeeper_servers)
    zk.start()

    # Get the number of Kafka brokers
    brokers = zk.get_children('/brokers/ids')
    broker_count = len(brokers)

    zk.stop()

    return broker_count

# Replace with your Zookeeper server(s)
zookeeper_servers = '192.168.1.241:2181'
print(f'Number of Kafka brokers: {get_broker_count(zookeeper_servers)}')
