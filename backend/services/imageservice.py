import cv2
import numpy as np
import base64

blur = (5, 5)
border_type = 0

lower_threshold = 50
upper_threshold = 150
image_scale = 1000

inter_mode = cv2.INTER_CUBIC


def convert_image(encoded):
    image_data = base64.b64decode(encoded)
    np_array = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_GRAYSCALE)
    return image


def split_image(image):
    blurred = cv2.GaussianBlur(image, blur, border_type)
    _, binary = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)
    edges = cv2.Canny(binary, lower_threshold, upper_threshold)
    cv2.imshow('image', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    height, width = image.shape[:2]
    min_area = height * width / image_scale
    filtered_contours = [c for c in contours if cv2.contourArea(c) > min_area]

    bounding_images = []
    for c in filtered_contours:
        x, y, w, h = cv2.boundingRect(c)
        cropped = image[y:y + h, x:x + w]
        bounding_images.append(cropped)
    
    return bounding_images


def resize_image(image, new_width, new_height):
    return cv2.resize(image, (new_width, new_height), interpolation=inter_mode)

def is_operator(image):
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return False