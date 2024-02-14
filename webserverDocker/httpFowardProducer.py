from flask import Flask, request
from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:9092'})
app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_frame():
    frame_data = request.data
    p.produce('webcam_topic', frame_data)
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
