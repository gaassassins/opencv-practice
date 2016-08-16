import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('panda.jpg')
img2 = cv2.imread('bird.jpg')
if img1.shape != img2.shape:

	img2 = cv2.resize(img2, img1.shape[:2][::-1])
	alpha = 0.5
	beta = 1 - alpha
	gamma = 0.0
	dst = cv2.addWeighted(img1, alpha, img2, beta, gamma)
        cv2.imshow('Image',dst)
	cv2.waitKey()

