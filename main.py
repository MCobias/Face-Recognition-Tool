import cv2
import numpy as np
from time import time
from utils.face_find import detect_face_align
from utils.mysql_connect import get_mysql_images
from utils.split_data import train_test_split_images
from utils.split_data import cross_validation_split_images
from utils.image_util import read_training_data

test_percent = 0.2

#start time
t0 = time()
print("--------------------")
print("   Preparing data   ")
print("--------------------")

db_list = get_mysql_images('frgc')

train_data, test_data =  train_test_split_images(db_list, test_percent)
#train_data, test_data = cross_validation_split_images(list, 2)

faces_train, label_train, image_name_train = read_training_data(train_data, '/media/psf/Home/Documents/Mestrado/Dataset faces/', 16)
faces_test, label_test, image_name_test = read_training_data(test_data, '/media/psf/Home/Documents/Mestrado/Dataset faces/', 16)

print("--------------------")
print("   Data prepared   ")
print("--------------------")

print("--------------------")
print("Total dataset size:")
print("Number of samples in dataset: %d" % len(db_list))
print("Number of classes in dataset: %d" % len(image_name_train))
print("--------------------")
print("Total train size: %d samples, %d%%" % (len(train_data), (1 - test_percent) * 100))
print("Total test size: %d samples, %d%%" % (len(test_data), test_percent * 100))
#print("Cross validation %d-fold" % cross_validation)
print("--------------------")

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces_train, np.array(label_train))

print("done in %0.3fs" % (time() - t0))

def predict(img_face):
    # predict the image using our face recognizer
    label, confidence = face_recognizer.predict(img_face)
    # get name of respective label returned by face recognizer
    label_text = label_train[label]




