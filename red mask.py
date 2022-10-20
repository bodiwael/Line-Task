import cv2
import numpy as np

frame = cv2.imread("/home/abdelrahman/line.jpeg")

hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

lower_red=np.array([0, 50, 50])             
upper_red=np.array([10, 255, 255])

mask_red=cv2.inRange(hsv,lower_red,upper_red)

res_red=cv2.bitwise_and(frame,frame,mask=mask_red)

cv2.imshow('Original',frame)

cv2.imshow('Mask_RED',mask_red)

cv2.imshow('Result RED',res_red)

cv2.waitKey(0)
cv2.destroyAllWindows()