from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    print(request.headers)
    kafka_topic = request.headers.get('kafka_topic')
    if kafka_topic:
        print(f'Received kafka_topic: {kafka_topic}')
        return 'Header received', 200
    else:
        return 'No kafka_topic header found', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
