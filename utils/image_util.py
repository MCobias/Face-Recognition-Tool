import cv2
import os
import numpy as np
import imghdr
from utils.face_find import detect_face_align

def read_training_data(list_images, data_folder, size):
    faces_train = []
    label_train = []
    image_name_train = []
    for image_name in list_images:
        if(is_valid_image(data_folder + image_name[15])):
            continue

        image = cv2.imread(data_folder + image_name[15])
        print("Image  <- " + image_name[1])
        face = detect_face_align(image, size)
        print("Person <- " + image_name[0])
        print("--")

        if face is not None:
            faces_train.append(face)
            label_train.append(image_name[0])
            image_name_train.append(image_name[1])
    return faces_train, label_train, image_name_train

def is_valid_image(str_image):
    ext = imghdr.what(str_image)
    if(ext == "jpeg"):
        return False
    elif(ext == "png"):
        return False
    elif(ext == "ppm"):
        return False
    else:
        return True
