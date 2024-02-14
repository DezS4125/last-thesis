import os
from flask import Flask, request
from confluent_kafka import Producer

# Read bootstrap servers from environment variables
bootstrap_servers = os.getenv('BOOTSTRAP_SERVERS')

# Initialize Kafka producer
p = Producer({'bootstrap.servers': bootstrap_servers})

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_frame():
    frame_data = request.data
    p.produce('webcam_topic', frame_data)

    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
