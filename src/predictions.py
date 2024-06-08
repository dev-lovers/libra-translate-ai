import tensorflow as tf
from keras.preprocessing import image
import numpy as np

import matplotlib.pyplot as plt
import requests
import json

class_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y']

def prepare_image(img_path, img_size):
    img = image.load_img(img_path, target_size=img_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0 
    return img_array

image_path = '../test_images/4.jpg'
x_test = prepare_image(image_path, (64, 64))

URL = "http://localhost:8501/v1/models/saved_model:predict"

def make_prediction(instances):
   data = json.dumps({"signature_name": "serving_default", "instances": instances.tolist()})
   headers = {"content-type": "application/json"}
   json_response = requests.post(URL, data=data, headers=headers)
   predictions = json.loads(json_response.text)['predictions']
   return predictions

predictions = make_prediction(x_test)
for i, pred in enumerate(predictions):
    predicted_class = class_names[np.argmax(pred)]
    print(f"Predicted Value: {predicted_class}")
