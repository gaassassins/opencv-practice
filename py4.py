import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cat.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([332,74,82])
upper_blue = np.array([317,64,82])

mask = cv2.inRange(hsv, lower_blue, upper_blue)

result_img = cv2.bitwise_and(img, img, mask=(255 - mask))

plt.subplot(1,3,1), plt.imshow(mask, 'gray')
plt.title('mask')
plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2), plt.imshow(img[:, :, ::-1])
plt.title('source')

plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3), plt.imshow(result_img[:, :, ::-1])
plt.title('result')
plt.xticks([]), plt.yticks([])
plt.show()

