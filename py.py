import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("hedgehog.jpg")
print("image size is: h:{0} w:{1} c:{2}".format(*img.shape))

plt.imshow(img[:, :, ::-1])
plt.xticks([]), plt.yticks([]) 
plt.show()


cap = cv2.VideoCapture(0)
while True:
	_, frame = cap.read()
	cv2.imshow("frame", frame)
	pressed_key = cv2.waitKey(30)

	if pressed_key == 27:
		break
