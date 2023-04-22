#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import cv2 as cv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
import keras
from keras import datasets, layers, models
from sklearn.preprocessing import LabelEncoder
import datasplit
tf.device('GPU:0')

print("importing done")


# In[6]:


df = pd.read_csv('trainLabels_cropped.csv')

X = df['image'].values
Y = df['level'].values


# In[7]:


def train_test_split(X, y, test_size):
    num_train_data_points = len(y) - int(len(y) * test_size)
    X_train, X_test = X[:num_train_data_points], X[num_train_data_points:]
    Y_train, Y_test = y[:num_train_data_points], y[num_train_data_points:]
    return X_train, X_test, Y_train, Y_test

def shuffle_data(X, y):
    indices = np.arange(X.shape[0])
    np.random.shuffle(indices)
    
    return X[indices], y[indices]


# In[8]:


X_train, X_test, Y_train, Y_test = datasplit.my_train_test_split(X,Y,0.2)
class_labels = ['No DR','Mild','Moderate','Severe','Proliferative DR']


# In[9]:


training_data = []
training_labels = []
size = (128,128)  # the desired size of the images
print("======================================train====================================")
for i in range(X_train.shape[0]):
    print("iteration:",i)
    path = os.path.join('resized_train_cropped',X_train[i])
    img = cv.imread(path+'.jpeg')
    img = cv.resize(img, size)  # resize the image
    training_data.append(img)
    training_labels.append(class_labels[Y_train[i]])

# convert each numpy array to tensor and stack them
training_data = tf.stack([tf.convert_to_tensor(img) for img in training_data])
le = LabelEncoder()
training_labels = le.fit_transform(training_labels)
training_labels = tf.convert_to_tensor(training_labels)


# In[10]:


testing_data = []
testing_labels = []
size = (128,128)  # the desired size of the images
print("==========================test===========================")
for i in range(X_test.shape[0]):
    print("iteration:",i)
    path = os.path.join('resized_train_cropped',X_test[i])
    img = cv.imread(path+'.jpeg')
    img = cv.resize(img, size)  # resize the image
    testing_data.append(img)
    testing_labels.append(class_labels[Y_test[i]])

# convert each numpy array to tensor and stack them
testing_data = tf.stack([tf.convert_to_tensor(img) for img in testing_data])
testing_labels = le.transform(testing_labels)
testing_labels = tf.convert_to_tensor(testing_labels)


# In[11]:


print(testing_data.shape[0])


# In[ ]:


print("Started training the model....")


model = models.Sequential()
model.add(layers.Conv2D(128, (7,7), activation='relu', input_shape = (128,128,3), padding='same', data_format='channels_first'))
model.add(layers.MaxPooling2D((6,6), padding='same', data_format='channels_last',strides=(1, 1)))

model.add(layers.Conv2D(128, (7,7), activation='relu', padding='same', data_format='channels_first'))
model.add(layers.MaxPooling2D((6,6), padding='same', data_format='channels_last',strides=(1, 1)))

model.add(layers.Conv2D(128, (7,7), activation='relu', padding='same', data_format='channels_first'))
model.add(layers.MaxPooling2D((6,6), padding='same', data_format='channels_last',strides=(1, 1)))

model.add(layers.Conv2D(128, (7,7), activation='relu', padding='same', data_format='channels_first'))
model.add(layers.MaxPooling2D((6,6), padding='same', data_format='channels_last',strides=(1, 1)))

model.add(layers.Conv2D(128, (7,7), activation='relu', padding='same', data_format='channels_first'))
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

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])

print("Fitting the model....")
# tf.device('GPU:0')
model.fit(training_data, training_labels, epochs = 10, validation_data = (testing_data,testing_labels))

loss, accuracy = model.evaluate(testing_data,testing_labels)



print("Done!!!")


loss, accuracy = model.evaluate(testing_data, testing_labels)
print(f"Loss = {loss}")
print(f"accuracy = {accuracy}")
model.save('predict_DR')


# In[ ]:


# Define a function to load the model and make predictions
# def predict_diabetic_retinopathy(image_path):
#     model = keras.models.load_model('model_diabetic_retinopathy')
#     size = (128,128)
#     img = cv.imread(image_path)
#     img = cv.resize(img, size)
#     img = tf.convert_to_tensor(img)

#     prediction = model.predict(img)
#     return prediction

def predict_diabetic_retinopathy(image_path, model_path='model_diabetic_retinopathy'):
    """
    This function takes an image path as input and returns a prediction of the severity of diabetic retinopathy.

    Args:
    - image_path (str): The path to the image file to be predicted.
    - model_path (str): The path to the trained model file. Default is 'model_diabetic_retinopathy'.

    Returns:
    - prediction (str): A string indicating the predicted severity of diabetic retinopathy. It can be one of:
                        - 'No DR'
                        - 'Mild'
                        - 'Moderate'
                        - 'Severe'
                        - 'Proliferative DR'
    """
    # Load the trained model
    model = keras.models.load_model(model_path)

    # Load the image and preprocess it
    size = (128, 128)
    img = cv.imread(image_path)
    img = cv.resize(img, size)
    img = np.array([img])
    # img = img / 255.0

    # Make a prediction using the model
    predictions = model.predict(img)
    prediction = np.argmax(predictions)

    # Map the prediction to the class label
    class_labels = ['No DR', 'Mild', 'Moderate', 'Severe', 'Proliferative DR']
    prediction = class_labels[prediction]

    return prediction
