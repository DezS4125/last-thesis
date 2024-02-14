import cv2
import requests

# Initialize video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Encode frame as JPEG
    ret, buffer = cv2.imencode('.jpg', frame)

    # Send frame to Kafka producer machine via HTTP
    requests.post('http://192.168.1.241:5000', data=buffer.tobytes())

# When everything done, release the capture
cap.release()
