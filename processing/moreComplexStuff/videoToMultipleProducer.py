import cv2
import requests
import uuid

# Initialize video capture
cap = cv2.VideoCapture(0)

# List of Kafka producer machines
kafka_producer_machines = ['http://producer1:5000', 'http://producer2:5000']

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Encode frame as JPEG
    ret, buffer = cv2.imencode('.jpg', frame)

    # Generate a unique identifier for the frame
    frame_id = str(uuid.uuid4())

    # Send frame and its identifier to each Kafka producer machine via HTTP
    for producer in kafka_producer_machines:
        requests.post(producer, json={'frame_id': frame_id, 'frame_data': buffer.tobytes().decode('iso-8859-1')})

# When everything done, release the capture
cap.release()
