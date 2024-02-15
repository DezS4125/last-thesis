import cv2
import requests
import os
import itertools

# Get environment variables
urls = os.getenv('URL').split(',')  # Assuming URLs are comma-separated
video_source = os.getenv('VIDEO_SOURCE')

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

    # Send frame to the selected server via HTTP
    requests.post(url, data=buffer.tobytes())

# When everything done, release the capture
cap.release()