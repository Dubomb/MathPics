from flask import Flask, Blueprint, request, jsonify
import base64
import sys

sys.path.append('../')
import services.predictservice as prs

predict_controller = Blueprint('predict_controller', __name__)

@predict_controller.post("/")
def predict_image():
    data = request.json
    encoded_image = data['image']

    with open('eqttest.jpg', 'rb') as f:
        bytes = f.read()
        prs.predict(base64.b64encode(bytes))

    response = {
        'prediction': 'Yes.'
    }

    return jsonify(response), 200