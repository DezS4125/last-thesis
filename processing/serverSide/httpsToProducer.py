from flask import Flask, request
from confluent_kafka import Producer
import numpy as np
import cv2

# Initialize Kafka producer
p = Producer({'bootstrap.servers': 'localhost:9092'})

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_frame():
    # Receive frame from HTTP request
    frame_data = request.data

    # Send frame to Kafka as bytes
    p.produce('webcam_topic', frame_data)

    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
