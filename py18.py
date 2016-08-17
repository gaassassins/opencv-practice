import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("2.jpg")
img2 = cv2.imread("1.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray, 50, 200)
canny2 = cv2.Canny(gray2, 50, 200)

_, contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

_, contours2, hierarchy2 = cv2.findContours(canny2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

max_distance = 1.0
nearest_contour = contours2[0]
goal_contour = contours[0]


for contour in contours2:
 curr_distance = cv2.matchShapes(goal_contour, contour, 3, 0)
 if curr_distance < max_distance:
  max_distance = curr_distance
  nearest_contour = contour

cv2.drawContours(img2, [nearest_contour], 0, (0, 255, 0), 3)
cv2.drawContours(img, contours, 0, (0, 0, 255), 3)

plt.subplot(1, 2, 1), plt.imshow(img)
plt.title('Image1')
plt.xticks([]), plt.yticks([])

plt.subplot(1, 2, 2), plt.imshow(img2)
plt.title('Image2')
plt.xticks([]), plt.yticks([])

plt.show()
