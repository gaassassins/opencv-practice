import cv2
import numpy as np
from matplotlib import pyplot as plt

def on_change(x):
        pass

cv2.namedWindow('Image')
cv2.createTrackbar('Value', 'Image', 0, 255, on_change)
img1 = cv2.VideoCapture(0)
lut = cv2.imread('lut2.png')

while True:
	_, frame = img1.read()
	img2 = cv2.LUT(frame, lut)
        val = cv2.getTrackbarPos('Value', 'Image')
        alpha = val / 255.0
        beta = 1 - alpha
        gamma = 0.0
        dst = cv2.addWeighted(frame, alpha, img2, beta, gamma)
        cv2.imshow('Image',dst)
        cv2.waitKey(30)

