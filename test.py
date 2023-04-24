import tensorflow as tf

tf.device('GPU:0')
import numpy as np
import pandas as pd

from tensorflow import keras
from tensorflow.keras import layers,models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical

class_weights = [0.7349322091830922, 0.26196082920149105, 0.7698358410031166, 0.5512822997723398, 0.9967366571835732]
class_labels = ['Notaffected','Mild','Moderate','Severe','Proliferative']

class_dict = {0: 0.7349322091830922, 1: 0.26196082920149105, 2: 0.7698358410031166, 3: 0.5512822997723398, 4: 0.9967366571835732}
# class_weights_dict = lambda class_labels, class_weights: {i: class_weights[i] for i in range(len(class_labels))}

# class_weights_dict(class_labels, class_weights)

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
integer_labels = le.fit_transform(class_labels)
# now convert integer labels to one-hot encoded labels
training_labels = to_categorical(integer_labels, num_classes=5)

batch_size = 32
img_size = (512,512)

train_datagen = ImageDataGenerator(
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
training_set = train_datagen.flow_from_directory('Train',
                                                 target_size = (512,512),
                                                 batch_size = 16,
                                                 class_mode = 'categorical')

test_datagen = ImageDataGenerator()
test_set = test_datagen.flow_from_directory('Validation',
                                            target_size = (512,512),
                                            batch_size = 16,
                                            class_mode = 'categorical')
test_labels = test_set.classes


model = models.Sequential()
model.add(layers.Conv2D(128, (7,7), activation='relu', input_shape = (512,512,3), padding='same', data_format='channels_first'))
model.add(layers.MaxPooling2D((6,6), padding='same', data_format='channels_last',strides=(1, 1)))

model.add(layers.Conv2D(128, (7,7), activation='relu', padding='same', data_format='channels_first'))
model.add(layers.MaxPooling2D((6,6), padding='same', data_format='channels_last',strides=(1, 1)))

model.add(layers.Conv2D(128, (7,7), activation='relu', padding='same', data_format='channels_first'))
model.add(layers.MaxPooling2D((6,6), padding='same', data_format='channels_last',strides=(1, 1)))

model.add(layers.Conv2D(128, (7,7), activation='relu', padding='same', data_format='channels_first'))
model.add(layers.MaxPooling2D((6,6), padding='same', data_format='channels_last',strides=(1, 1)))

model.add(layers.Conv2D(128, (7,7), activation='relu', padding='same', data_format='channels_first'))
model.add(layers.MaxPooling2D((6,6), padding='same', data_format='channels_last',strides=(1, 1)))

model.add(layers.Conv2D(128, (7,7), activation='relu', padding='same', data_format='channels_first'))
model.add(layers.MaxPooling2D((6,6), padding='same', data_format='channels_last',strides=(1, 1)))

model.add(layers.Conv2D(128, (7,7), activation='relu', padding='same', data_format='channels_first'))
model.add(layers.MaxPooling2D((6,6), padding='same', data_format='channels_last',strides=(1, 1)))

model.add(layers.Conv2D(128, (7,7), activation='relu', padding='same', data_format='channels_first'))
model.add(layers.MaxPooling2D((6,6), padding='same', data_format='channels_last',strides=(1, 1)))

model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(5, activation='sigmoid'))
print("Compiling...")

model.compile(optimizer='adam', loss='categorical_crossentropy',metrics=['accuracy'])

print("Fitting the model....")

model.fit(x=training_set, validation_data=(test_set), epochs=3, verbose=1,class_weight = class_dict)

model.save('Balanced_Diabetic_Retinopathy_Prediction')