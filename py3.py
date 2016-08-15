import cv2
import numpy as np
from matplotlib import pyplot as plt

channels_HSV = ['H', 'S', 'V']
channels_RGB = ['B', 'G', 'R']
channels_Lab = ['L', 'a', 'b']
img = cv2.imread('panda.jpg')
for index in range(3):
	plt.subplot(3, 3, index +1), plt.imshow(img[:, :, index], 'gray')
	plt.title(channels_RGB[index])
	plt.xticks([]), plt.yticks([])

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
for index in range(3):
	plt.subplot(3, 3, 3 + index +1), plt.imshow(hsv[:, :, index], 'gray')
	plt.title(channels_HSV[index])
	plt.xticks([]), plt.yticks([])


Lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
for index in range(3):
	plt.subplot(3, 3, 6 + index + 1), plt.imshow(Lab[:, :, index], 'gray')
	plt.title(channels_Lab[index])
	plt.xticks([]), plt.yticks([])
plt.show()
