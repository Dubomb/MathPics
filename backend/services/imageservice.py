import cv2
import numpy as np
import base64
import random
import os
import torch
from torchvision import transforms

blur = (5, 5)
border_type = 0

lower_threshold = 50
upper_threshold = 150
image_scale = 1000

inter_mode = cv2.INTER_CUBIC


def decode_image(encoded):
    image_data = base64.b64decode(encoded)
    np_array = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_GRAYSCALE)
    return image


def split_image(image):
    blurred = cv2.GaussianBlur(image, blur, border_type)
    _, binary = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)
    edges = cv2.Canny(binary, lower_threshold, upper_threshold)
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    height, width = image.shape[:2]
    min_area = height * width / image_scale
    filtered_contours = [c for c in contours if cv2.contourArea(c) > min_area]

    bounding_images = []
    for contour in filtered_contours:
        x, y, w, h = cv2.boundingRect(contour)
        cx = x + w // 2
        cy = y + h // 2
        largest_dim = max(abs(cx - x), abs(cy - y))
        x = cx - largest_dim
        w = largest_dim * 2
        y = cy - largest_dim
        h = largest_dim * 2

        cropped = image[y:y+h, x:x + w]
        bounding_images.append((x, cropped))

    bounding_images.sort(key=lambda image : image[0])
    return bounding_images


def add_background(image, bg_width, bg_height, padding):
    im_size = bg_width - padding * 2
    curr_height, curr_width = image.shape[:2]
    if curr_height > curr_width:
        scale = im_size / curr_height
    else:
        scale = im_size / curr_width
    curr_width = int(curr_width * scale)
    curr_height = int(curr_height * scale)
    resized = cv2.resize(image, (curr_width, curr_height), interpolation=cv2.INTER_CUBIC)
    bg = np.full((bg_width, bg_height), 255, dtype=np.uint8)
    bg_xpos = (bg_width - curr_width) // 2
    bg_ypos = (bg_height - curr_height) // 2
    bg[bg_ypos:bg_ypos+curr_height, bg_xpos:bg_xpos+curr_width] = resized
    return bg


def transform_image(image):
    transformed_image = torch.tensor(image, dtype=torch.float32)
    input_image = transformed_image.unsqueeze(0)
    return input_image
