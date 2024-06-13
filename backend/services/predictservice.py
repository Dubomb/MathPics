import numpy as np
from . import imageservice as ims
import cv2

def predict(encoded_image):
    decoded_image = ims.convert_image(encoded_image)

    symbol_images = ims.split_image(decoded_image)

    for symbol in symbol_images:
        bg = ims.add_background(symbol, 150, 150, 20)
        cv2.imshow('padded', bg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()