import cv2
import imutils
import sys
from imutils import face_utils
import numpy as np
import argparse
import dlib
from imutils.face_utils import FaceAligner

def detect_face_align(img, size=0):
    # convert the test image to gray image as opencv face detector expects gray images
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detector = dlib.get_frontal_face_detector()

    predictor = dlib.shape_predictor('data/shape_predictor_68_face_landmarks.dat')
    fa = FaceAligner(predictor, desiredFaceWidth=256)
    faces = detector(img_gray, 1)

    if (len(faces) == 0):
        return None

    shape = predictor(img_gray, faces[0])
    left_eye = extract_left_eye_center(shape)
    right_eye = extract_right_eye_center(shape)

    height, width = img.shape[:2]
    (x, y, w, h) = get_face_bbox_from_landmarks(shape)

    mat = get_rotation_matrix(left_eye, right_eye)
    rotated = cv2.warpAffine(img_gray, mat, (width, height), flags=cv2.INTER_CUBIC)
    #cropped =

    if(size):
        return imutils.resize(rotated[y:y + h, x:x + w], width=size)
    else:
        return rotated[y:y + h, x:x + w]

def get_face_bbox_from_landmarks(shape):
    landmarks = []
    shape = face_utils.shape_to_np(shape)
    for (name, (i, j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
        for (x, y) in shape[i:j]:
            landmarks.append(tuple((name, x, y)))

    xmax, ymax = 0, 0
    xmin, ymin = sys.maxsize, sys.maxsize
    for (name, x, y) in landmarks:
        if x < xmin:
            xmin = x
        elif x > xmax:
            xmax = x
        elif y < ymin:
            ymin = y
        elif y > ymax:
            ymax = y
    return [xmin, ymin, xmax - xmin, ymax - ymin]

#Using some code from: https://github.com/nlhkh/face-alignment-dlib

LEFT_EYE_INDICES = [36, 37, 38, 39, 40, 41]
RIGHT_EYE_INDICES = [42, 43, 44, 45, 46, 47]

def rect_to_tuple(rect):
    left = rect.left()
    right = rect.right()
    top = rect.top()
    bottom = rect.bottom()
    return left, top, right, bottom

def extract_eye(shape, eye_indices):
    points = map(lambda i: shape.part(i), eye_indices)
    return list(points)

def extract_eye_center(shape, eye_indices):
    points = extract_eye(shape, eye_indices)
    xs = map(lambda p: p.x, points)
    ys = map(lambda p: p.y, points)
    return sum(xs) // 6, sum(ys) // 6

def extract_left_eye_center(shape):
    return extract_eye_center(shape, LEFT_EYE_INDICES)

def extract_right_eye_center(shape):
    return extract_eye_center(shape, RIGHT_EYE_INDICES)

def angle_between_2_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    tan = (y2 - y1) / (x2 - x1)
    return np.degrees(np.arctan(tan))

def get_rotation_matrix(p1, p2):
    angle = angle_between_2_points(p1, p2)
    x1, y1 = p1
    x2, y2 = p2
    xc = (x1 + x2) // 2
    yc = (y1 + y2) // 2
    M = cv2.getRotationMatrix2D((xc, yc), angle, 1)
    return M

def crop_image(image, det):
    left, top, right, bottom = rect_to_tuple(det)
    return image[top:bottom, left:right]

def resize_image(img, size):
    return imutils.resize(img, width=size)