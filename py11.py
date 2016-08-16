import cv2
import numpy as np
from matplotlib import pyplot as plt
 
 
IMG_PATH = 'hedgehog.jpg'
ITER_COUNT = 5
ksize = 5
 
img = cv2.imread(IMG_PATH)
 
drawing = False
top_left_x, top_left_y = 0, 0
bottom_right_x, bottom_right_y = 0, 0
mouse_image = cv2.imread(IMG_PATH)
 
def mouse_callback(e, x, y, flags, params) :
    global top_left_x, top_left_y, bottom_right_x, bottom_right_y, drawing, mouse_image
 
    if e == cv2.EVENT_LBUTTONDOWN :
        drawing = True
        top_left_x, top_left_y = x, y
    elif e == cv2.EVENT_MOUSEMOVE :
        if drawing :
            mouse_image = cv2.imread(IMG_PATH)
            cv2.rectangle(mouse_image, (top_left_x, top_left_y), (x, y), (255, 0, 0), 2) # last param -1 - to fill, 1 - to empty rectangle
    elif e == cv2.EVENT_LBUTTONUP :
        bottom_right_x, bottom_right_y = x, y
        drawing = False
 
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_callback)
 
while True:
    cv2.imshow('Image', mouse_image)
    pressed_key = cv2.waitKey(30)
    if pressed_key == 27 :
        break
 
    if pressed_key == 32 :
        mouse_image = cv2.imread(IMG_PATH)
        mask = np.zeros((mouse_image.shape[0], mouse_image.shape[1]), np.uint8)
        rect = (min(top_left_x, bottom_right_y), min(top_left_y, bottom_right_y), abs(bottom_right_x - top_left_x), abs(bottom_right_y - top_left_y))
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)
 
        cv2.grabCut(mouse_image, mask, rect, bgdModel, fgdModel, ITER_COUNT, cv2.GC_INIT_WITH_RECT)
 
        mask_image = (mask & 1)
	mask_image = cv2.cvtColor(mask_image, cv2.COLOR_GRAY2BGR)

	res = mask_image * mouse_image
	bgd = cv2.GaussianBlur(mouse_image, (19,19), 11) * (1 - mask_image)
	result = cv2.add (res, bgd)
	cv2.imshow('foregroud', result)
	cv2.waitKey() 	
