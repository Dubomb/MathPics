import numpy as np
from . import imageservice as ims
import cv2
import torch

from . import model_linear as ml

prediction_map = {
    0: '+',
    1: '/',
    2: '8',
    3: '5',
    4: '4',
    5: '*',
    6: '9',
    7: '1',
    8: '7',
    9: '6',
    10: '-',
    11: '3',
    12: '2',
    13: '0',
}

def get_prediction(image):
    model = ml.ModelLinear()
    model.load_state_dict(torch.load('../services/model_linear.pt', torch.device('cpu')))
    input = ims.transform_image(image)
    with torch.no_grad():
        output = model(input)
        prediction = output.argmax(1).item()
    return prediction_map[prediction]

def predict(encoded_image):
    decoded_image = ims.decode_image(encoded_image)

    symbol_images = ims.split_image(decoded_image)

    equation = ''
    for _, symbol in symbol_images:
        bg = ims.add_background(symbol, 32, 32, 2)
        cv2.imshow('image', bg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        equation += get_prediction(bg)
    print(f'equation {equation} = {eval(equation)}')