import cv2
from utils.face_find import detect_face_align
from utils.mysql_connect import get_mysql_images
from utils.split_data import train_test_split_images
from utils.split_data import cross_validation_split_images
from utils.image_util import read_training_data


print("Preparing data...")

#test = cv2.imread('/media/psf/Home/Documents/Mestrado/Dataset faces/FRGC-2.0-dist/nd1/Fall2002/2002-247/04514d04.JPG')
#face = detect_face_align(test, 512)
#cv2.imshow('Face', face)
#cv2.waitKey(0)

list = get_mysql_images('frgc')
read_training_data(list, '/media/psf/Home/Documents/Mestrado/Dataset faces/', 32)
#print(list[0])



#train_data, test_data =  train_test_split_images(list, 0.2)
#print(len(train_data))
#cross_validation_split_images(list, 2)



