from . import imageservice as ims

def predict(encoded_image):
    ims.init_templates()

    decoded_image = ims.convert_image(encoded_image)

    symbol_images = ims.split_image(decoded_image)

    for symbol in symbol_images:
        resized = ims.resize_image(symbol, 28, 28)
        print(ims.is_operator(resized))