m#loop-up-tables

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('panda.jpg')
lut = cv2.imread('lut1.png')
dst = cv2.LUT(img,lut)

while True:
	cv2.imshow('Image',dst)

	pressed_key = cv2.waitKey(30)

	if pressed_key == 27:
		break
