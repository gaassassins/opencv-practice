import cv2
import numpy as np
from matplotlib import pyplot as plt

drawing = False
curr_x, curr_y = 0, 0
mouse_image = np.zeros((400, 400, 1), np.uint8)

def mouse_callback(e, x, y, flags, param):
	global curr_x, curr_y, drawing, mouse_image
	if e == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		curr_x, curr_y = x, y
	elif e == cv2.EVENT_MOUSEMOVE:
		if drawing:
			mouse_image = np.zeros((400, 400, 1), np.uint8)
			cv2.rectangle(mouse_image, (curr_x, curr_y), (x, y), 255, -1)
	elif e == cv2.EVENT_LBUTTONUP:
		drawing = False

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_callback)

while True:
	cv2.imshow('Image', mouse_image)
	pressed_key = cv2.waitKey(30)
	if pressed_key == 27:
		break
