import cv2
import numpy as np
from matplotlib import pyplot as plt

def on_change(x):
	pass

cv2.namedWindow('Image')

cv2.createTrackbar('Low', 'Image', 0, 255, on_change)
cv2.createTrackbar('Hight', 'Image', 0, 255, on_change)

cap = cv2.VideoCapture(0)

while True:
	low = cv2.getTrackbarPos('Low', 'Image')
	up = cv2.getTrackbarPos('Hight', 'Image')

	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	lower = np.array([low, 80, 80])
	upper = np.array([up,255,255])

	mask = cv2.inRange(hsv, lower, upper)

	result_img = cv2.bitwise_and(frame, frame, mask=(255 - mask))
	cv2.imshow('Image', result_img)	

	pressed_key = cv2.waitKey(30)

	if pressed_key == 27:
		break
