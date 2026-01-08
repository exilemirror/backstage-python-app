from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/')

def home():
    return '<h1>Welcome to Backstage Python App</h1>'

@app.route('/api/v1/details')

def details():
    return jsonify({
        "message": "Welcome to the Details page.",
        "time": datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        "hostname": socket.gethostname(),
        "message": "Custard Pie"

    })

@app.route('/api/v1/healthz')

def health():
    return jsonify({
        "status": "up"
    }), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0")