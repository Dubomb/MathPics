from . import imageservice as ims

def predict(encoded_image):
    decoded_image = ims.convert_image(encoded_image)

    symbol_images = ims.split_image(decoded_image)

    for symbol in symbol_images:
        resized = ims.resize_image(symbol)
        print(ims.is_operator(symbol))