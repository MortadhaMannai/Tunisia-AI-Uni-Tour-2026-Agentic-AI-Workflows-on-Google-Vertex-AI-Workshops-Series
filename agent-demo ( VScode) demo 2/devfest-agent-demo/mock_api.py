# mock_api.py
from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route("/data")
def data():
    value = random.uniform(10, 100)
    features = {
        "f1": value + random.normalvariate(0, 5),
        "f2": random.normalvariate(0, 1),
        "f3": random.randint(0, 9)
    }
    payload = {
        "timestamp": int(time.time()),
        "value": value,
        "features": features
    }
    return jsonify(payload)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
