from flask import Flask
from predictcontroller import predict_controller

app = Flask(__name__)
app.register_blueprint(predict_controller, url_prefix='/predict')