import cv2
import numpy as np
from matplotlib import pyplot as plt

def on_change(x):
	pass

img = np.zeros((400,400,1), np.uint8)
cv2.namedWindow('Image')
cv2.createTrackbar('Value', 'Image', 0, 255, on_change)

while True:
        val = cv2.getTrackbarPos('Value', 'Image')
        img[:] = val
        cv2.imshow('Image', img)
        cv2.waitKey(10)
	pressed_key = cv2.waitKey(30)
	if pressed_key == 27:
		break
