import cv2
from kafka import KafkaProducer
from kafka.errors import KafkaError
# from CONSTANT import BOOTSTRAP_SERVERS
# import preprocessing.detectFaceYolov8 as det
# from confluent_kafka.admin import AdminClient

# video_topic_input='video'

# # logging.basicConfig(level=logging.DEBUG)
# admin_client = AdminClient({'bootstrap.servers': '192.168.1.241:9092'})
# existing_topics = admin_client.list_topics().topics

# i = 1
# while True:
#     topic_name = f"{video_topic_input}-{i}"
#     if topic_name not in existing_topics:
#         break
#     i += 1

# Set up the Kafka producer
producer = KafkaProducer(bootstrap_servers='192.168.1.241:9092')

# Set up the video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    print("####################")
    # frame=det.processOneFaceInFrame(frame)

    # Encode the frame as a JPEG image
    ret, jpeg = cv2.imencode('.jpg', frame)
    # Send the encoded frame to the Kafka topic
    future = producer.send('topic_name', jpeg.tobytes())
    print("Message sent!")
    
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError as e:
        # Decide what to do if produce request failed...
        print ("Message sent failed")
        print (f"Error: {e}")
        pass
    # cap.release()

# Release the video capture when done
cap.release()