from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.post("/predict/")
def predict_image():
    data = request.json
    encoded_image = data['image']

    response = {
        'prediction': 'Yes.'
    }

    return jsonify(response), 200