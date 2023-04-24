import shutil
import pandas as pd
import numpy as np
import os
import cv2 as cv
import sys


def move_file(src_file, dst_dir):
    shutil.move(src_file, dst_dir)

df = pd.read_csv('trainLabels_cropped.csv')

def shuffle_data(X, y):
    X = X.reset_index(drop = True)
    y = y.reset_index(drop = True)
    indices = np.arange(X.shape[0])
    np.random.shuffle(indices)
    
    return X[indices], y[indices]

def my_train_test_split(X, y, test_size):
    X , y = shuffle_data(X, y)
    num_train_data_points = len(y) - int(len(y) * test_size)
    X_train, X_test = X[:num_train_data_points], X[num_train_data_points:]
    Y_train, Y_test = y[:num_train_data_points], y[num_train_data_points:]

    return X_train, X_test, Y_train, Y_test

class0_images = df.loc[df['level'] == 0, 'image'].head(700)
class1_images = df.loc[df['level'] == 1, 'image'].head(700)
class2_images = df.loc[df['level'] == 2, 'image'].head(700)
class3_images = df.loc[df['level'] == 3, 'image'].head(700)
class4_images = df.loc[df['level'] == 4, 'image'].head(700)


class0_labels = df.loc[df['level'] == 0, 'level'].head(700)
class1_labels = df.loc[df['level'] == 1, 'level'].head(700)
class2_labels = df.loc[df['level'] == 2, 'level'].head(700)
class3_labels = df.loc[df['level'] == 3, 'level'].head(700)
class4_labels = df.loc[df['level'] == 4, 'level'].head(700)

# print(class0_images.shape)
# print(class1_images.shape)
# print(class2_images.shape)
# print(class3_images.shape)
# print(class4_images.shape)





class0_train_images, class0_test_images, class0_train_labels, class0_test_labels = my_train_test_split(class0_images,class0_labels,0.2)
class1_train_images, class1_test_images, class1_train_labels, class1_test_labels = my_train_test_split(class1_images,class1_labels,0.2)
class2_train_images, class2_test_images, class2_train_labels, class2_test_labels = my_train_test_split(class2_images,class2_labels,0.2)
class3_train_images, class3_test_images, class3_train_labels, class3_test_labels = my_train_test_split(class3_images,class3_labels,0.2)
class4_train_images, class4_test_images, class4_train_labels, class4_test_labels = my_train_test_split(class4_images,class4_labels,0.2)

print("Transferring....")
for i in class0_train_images:
    i += '.jpeg'
    path = os.path.join('images',str(i)) 
    cwd = os.path.abspath(".") 
    new_dir = "Train\\No_DR"
    dest = os.path.join(cwd, new_dir)
    shutil.copy(path,dest)

for i in class1_train_images:
    i += '.jpeg'
    path = os.path.join('images',str(i))
    cwd = os.path.abspath(".")  
    new_dir = "Train\Mild"
    dest = os.path.join(cwd, new_dir)
    shutil.copy(path,dest)

for i in class2_train_images:
    i += '.jpeg'
    path = os.path.join('images',str(i))
    cwd = os.path.abspath(".")  
    new_dir = "Train_Balanced\Moderate"
    dest = os.path.join(cwd, new_dir)
    shutil.copy(path,dest)

for i in class3_train_images:
    i += '.jpeg'
    path = os.path.join('images',str(i))    
    cwd = os.path.abspath(".") 
    new_dir = "Train_Balanced\Severe"
    dest = os.path.join(cwd, new_dir)
    shutil.copy(path,dest)

for i in class4_train_images:
    i += '.jpeg'
    path = os.path.join('images',str(i))    
    cwd = os.path.abspath(".")  
    new_dir = "Train_Balanced\Proliferative"
    dest = os.path.join(cwd, new_dir)
    shutil.copy(path,dest)


print("Done")

for i in class0_test_images:
    i += '.jpeg'
    path = os.path.join('images',str(i))
    cwd = os.path.abspath('.')
    new_dir = "Validation\\No_DR"
    dest = os.path.join(cwd, new_dir)
    shutil.copy(path,dest)

for i in class1_test_images:
    i += '.jpeg'
    path = os.path.join('images',str(i))
    cwd = os.path.abspath('.')
    new_dir = "Validation_Balanced\Mild"
    dest = os.path.join(cwd, new_dir)
    shutil.copy(path,dest)

for i in class2_test_images:
    i += '.jpeg'
    path = os.path.join('images',str(i))
    cwd = os.path.abspath('.')
    new_dir = "Validation_Balanced\Moderate"
    dest = os.path.join(cwd, new_dir)
    shutil.copy(path,dest)

for i in class3_test_images:
    i += '.jpeg'
    path = os.path.join('images',str(i))
    cwd = os.path.abspath('.')
    new_dir = "Validation_Balanced\Severe"
    dest = os.path.join(cwd, new_dir)
    shutil.copy(path,dest)

for i in class4_test_images:
    i += '.jpeg'
    path = os.path.join('images',str(i))
    cwd = os.path.abspath('.')
    new_dir = "Validation_Balanced\Proliferative"
    dest = os.path.join(cwd, new_dir)
    shutil.copy(path,dest)

print("done!!")