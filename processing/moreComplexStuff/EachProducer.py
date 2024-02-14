from flask import Flask, request
from confluent_kafka import Producer
import numpy as np
import cv2

# Initialize Kafka producer
p = Producer({'bootstrap.servers': 'localhost:9092'})

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_frame():
    # Receive frame and its identifier from HTTP request
    frame_id = request.json['frame_id']
    frame_data = request.json['frame_data'].encode('iso-8859-1')

    # Convert frame data back to numpy array
    frame = np.frombuffer(frame_data, dtype=np.uint8)

    # Decode frame as JPEG
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

    # Send frame to Kafka as bytes, using the frame identifier as the key
    p.produce('webcam_topic', key=frame_id, value=frame.tobytes())

    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
