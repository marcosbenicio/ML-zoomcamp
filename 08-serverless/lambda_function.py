import tflite_runtime.interpreter as tflite

import os
from io import BytesIO
from urllib import request
from PIL import Image
import numpy as np

def download_image(url):
    # Open the URL, read the content and store it in a buffer (temporarily holding data in memory)
    with request.urlopen(url) as resp:
        buffer = resp.read()
    # Create a BytesIO stream from the buffer
    stream = BytesIO(buffer)
    # Open the stream as an Image object
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    """Convert image to 'RGB' mode and resize it to the target size.

    Args:
        img: Image object to be converted and resized.
        target_size : A tuple (width, height) for the target size.

    Returns:
        The converted and resized image
    """
    if img.mode != 'RGB':
        img = img.convert('RGB')
    # Resize the image to the target size using the NEAREST filter
    img = img.resize(target_size, Image.NEAREST)
    return img

interpreter = tflite.Interpreter(model_path = "bees-wasps-v2.tflite")
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

def predict(url):
    img = download_image(url)
    img = prepare_image(img, target_size=(150, 150))

    img = np.array(img, dtype='float32')/255.0
    img = img[None,:,:,:]

    interpreter.set_tensor(input_index, img)
    interpreter.invoke()
    pred = interpreter.get_tensor(output_index)

    return float(pred[0][0])


def lambda_handler(event, context):
    url = event['url']
    pred = predict(url)
    result = {'prediction': pred}

    return result