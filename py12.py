import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('panda.jpg', 0)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = 5)
titles = ['laplacian', 'sobelx', 'sobely']
images = [laplacian, sobelx, sobely]

for index, image in enumerate (images):
	plt.subplot(1,3, index +1)
	plt.imshow(images[index], cmap = 'gray')
	plt.title(titles[index])
	plt.xticks([]), plt.yticks([])
plt.show()
