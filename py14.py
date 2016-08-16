import cv2
import numpy as np
from matplotlib import pyplot as plt

def on_change(x):
        pass

cv2.namedWindow('Image')
cv2.createTrackbar('t1', 'Image', 0, 255, on_change)
cv2.createTrackbar('t2', 'Image', 0, 255, on_change)
cap = cv2.VideoCapture(0)

while True:
	t1 = cv2.getTrackbarPos('t1', 'Image')
	t2 = cv2.getTrackbarPos('t2', 'Image')
	_, frame = cap.read()
        canny_image = cv2.Canny(frame, t1, t2)
        cv2.imshow('Image', canny_image)
        key = cv2.waitKey(30)
        if key == 27:
                break

