# 1. Importação das bibliotecas e a base de dados

import os
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Configurações
dataset_directory = os.path.join(os.getcwd(), 'dataset')
training_dataset_directory = os.path.join(dataset_directory, 'train')
validation_dataset_directory = os.path.join(dataset_directory, 'validation')

image_height, image_width = 64, 64
image_size = (image_height, image_width)

batch_size = 32
epochs = 10  # Reduzido o número de épocas para acelerar o treinamento
learning_rate = 0.0001

# 2 - Pré-processamento
training_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.1,  # Reduzido para menos distorção
    zoom_range=0.1,   # Reduzido para menos distorção
    horizontal_flip=True
)

validation_datagen = ImageDataGenerator(rescale=1./255)

training_generator = training_datagen.flow_from_directory(
    training_dataset_directory,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='categorical'
)

validation_generator = validation_datagen.flow_from_directory(
    validation_dataset_directory,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='categorical'
)

# 3 - Construção do modelo
model = Sequential([
    Conv2D(16, (3, 3), activation='relu', input_shape=(image_height, image_width, 3)),
    MaxPooling2D(2, 2),
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dropout(0.5),
    Dense(128, activation='relu'),
    Dense(21, activation='softmax')  # Certifique-se de que o número de classes esteja correto
])

# 4 - Compilação
model.compile(optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 5 - Treinando o modelo
history = model.fit(
    training_generator,
    epochs=epochs,
    validation_data=validation_generator,
    verbose=1
)

# 6 - Salvando o modelo
model.save('./models/keras/model.keras')
# tf.saved_model.save(model, './models/saved_model/model')
print('Modelo treinado e salvo com sucesso!')
