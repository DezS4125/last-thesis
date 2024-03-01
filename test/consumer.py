 
from kafka import KafkaConsumer
import cv2
import numpy as np

# Set up the Kafka consumer
consumer = KafkaConsumer('video-stream-2', bootstrap_servers='192.168.1.241:9092')

for message in consumer:
    # The message value is the bytes of the image
    image_bytes = message.value

    # Convert the bytes to a numpy array
    nparr = np.frombuffer(image_bytes, np.uint8)

    # Decode the numpy array as an image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Display the image
    cv2.imshow('image', img)
    cv2.waitKey(1)  # If you want the image window to close on a key press, use cv2.waitKey(0)

cv2.destroyAllWindows()  # Make sure to include this so the image windows close properly
