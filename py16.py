import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 50, 200)

_, contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

if contours:
 max_area = 0.0
 max_contour = contours[0]
 for contour in contours:
  c_area = cv2.contourArea(contour)
  if c_area > max_area:
   max_area = c_area
   max_contour = contour
 cv2.drawContours(img, [max_contour], 0, (0, 255, 0), 3)
 cv2.imshow('Image', img)
 cv2.waitKey()
