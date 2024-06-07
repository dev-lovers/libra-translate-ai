import tensorflow as tf
from keras.preprocessing import image
import numpy as np

# Carregar o modelo salvo
model = tf.keras.models.load_model('./models/bsl-ai.keras')

class_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y']

# Função para carregar e preparar a imagem
def prepare_image(img_path, img_size):
    img = image.load_img(img_path, target_size=img_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalização
    return img_array

img_path = '../data/test_images/6.jpg'
prepared_image = prepare_image(img_path, (64, 64))

predictions = model.predict(prepared_image)

# Obter a classe prevista
predicted_index = np.argmax(predictions, axis=-1)[0]
predicted_class_name = class_names[predicted_index]
print(f'Classe prevista: {predicted_class_name}')
