import cv2
import os
import numpy as np
from utils.face_find import detect_face_align

def read_training_data(list_images, data_folder, size):
    faces_train = []
    for image_name in list_images:
        if image_name[15].startswith("."):
            continue

        print(data_folder + image_name[15])
        image = cv2.imread(data_folder + image_name[15])

        print("Detecting face in image: " + image_name[1])

        face = detect_face_align(image, size)
        print("Training Label: " + image_name[0])

        if face is not None:
            faces_train.append((image_name[0], face))
    return faces_train
