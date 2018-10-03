import numpy
import random
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

def train_test_split_images(list_images, test_size):
    random.shuffle(list_images)
    train, test = train_test_split(list_images, test_size=test_size)
    return train, test

def cross_validation_split_images(list_images, kfolds):
    x_train = []
    x_test = []
    random.shuffle(list_images)
    kf = KFold(n_splits=kfolds)
    kf.get_n_splits(list_images)
    for train_index, test_index in kf.split(list_images):
        list_aux = []
        for i in train_index:
            list_aux.append(list_images[i])
        x_train.append(list_aux)
        list_aux = []
        for k in test_index:
            list_aux.append(list_images[k])
        x_test.append(list_aux)
    return x_train, x_test
