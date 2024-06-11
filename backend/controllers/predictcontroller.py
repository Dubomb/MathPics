from flask import Flask, request, jsonify
import base64
import sys

sys.path.append('../')
import services.predictservice as prs

app = Flask(__name__)

@app.post("/predict/")
def predict_image():
    data = request.json
    encoded_image = data['image']

    with open('eqt.jpg', 'rb') as f:
        bytes = f.read()
        prs.predict(base64.b64encode(bytes))

    response = {
        'prediction': 'Yes.'
    }

    return jsonify(response), 200