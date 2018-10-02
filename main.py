import cv2
from utils.face_find import detect_face_align

test = cv2.imread('/media/psf/Home/Documents/Mestrado/Dataset faces/FRGC-2.0-dist/nd1/Fall2002/2002-240/04212d53.JPG')
face = detect_face_align(test, 256)

cv2.imshow('Face', face)
cv2.waitKey(0)
