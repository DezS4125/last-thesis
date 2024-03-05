import cv2
import requests
import os
import itertools
import time

# Get environment variables
urls = os.getenv('URL','http://192.168.1.241:5000').split(',')  # Assuming URLs are comma-separated
video_source = os.getenv('VIDEO_SOURCE','0')
kafka_topic = os.getenv('KAFKA_TOPIC','video-stream-1')
max_fps = int(os.getenv('MAX_FPS','60'))

print('URLs: ')
for url in urls:
    print('- ' + url)
print('Video Source: ', video_source)
print('Kafka Topic: ', kafka_topic)
print('Max FPS: ', max_fps)

# Check if VIDEO_SOURCE can be converted to an integer
try:
    video_source = int(video_source)
except ValueError:
    pass  # VIDEO_SOURCE is a string, treat it as a video file path

# Initialize video capture
cap = cv2.VideoCapture(video_source)

# Create an iterator that produces URLs in a cyclic manner
url_iterator = itertools.cycle(urls)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Encode frame as JPEG
    ret, buffer = cv2.imencode('.jpg', frame)

    # Get the next URL from the iterator
    url = next(url_iterator)
    headers = {'kafka-topic':kafka_topic}

    # Send frame to the selected server via HTTP
    requests.post(url, data=buffer.tobytes(),headers=headers)
    
    print(max_fps)
    time.sleep(1/max_fps)

# When everything done, release the capture
cap.release()