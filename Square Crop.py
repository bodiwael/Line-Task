import cv2

img = cv2.imread("/home/abdelrahman/lin.jpeg")

(h, w) = img.shape[:2]

centerx, centery = (w // 14), (h // 14)

sq_1 = img[0 : centery, 0 : centerx]

sq_2 = img[0 : centery, centerx : centerx*4]

sq_3 = img[0 : centery, centerx*4 : centerx*7]

sq_4 = img[0 : centery, centerx*7 : centerx*10]

sq_5 = img[0 : centery, centerx*10 : centerx*13]

sq_6 = img[0 : centery, centerx*13 : w]

sq_7 = img[centery*2 : centery*5, 0 : centerx]

sq_8 = img[centery*2 : centery*5, centerx : centerx*4]

sq_9 = img[centery*2 : centery*5, centerx*4 : centerx*7]

sq_10 = img[centery*2 : centery*5, centerx*7 : centerx*10]

sq_11 = img[centery*2 : centery*5, centerx*10 : centerx*13]

sq_12 = img[centery*2 : centery*5, centerx*13 : w]

sq_13 = img[centery*5 : centery*9, 0 : centerx]

sq_14 = img[centery*5 : centery*9, centerx : centerx*4]

sq_15 = img[centery*5 : centery*9, centerx*4 : centerx*7]

sq_16 = img[centery*5 : centery*9, centerx*7 : centerx*10]

sq_17 = img[centery*5 : centery*9, centerx*10 : centerx*13]

sq_18 = img[centery*5 : centery*9, centerx*13 : w]

sq_19 = img[centery*9 : centery*13, 0 : centerx]

sq_20 = img[centery*9 : centery*13, centerx : centerx*4]

sq_21 = img[centery*9 : centery*13, centerx*4 : centerx*7]

sq_22 = img[centery*9 : centery*13, centerx*7 : centerx*10]

sq_23 = img[centery*9 : centery*13, centerx*10 : centerx*13]

sq_24 = img[centery*9 : centery*13, centerx*13 : w]

sq_25 = img[centery*13 : h, 0 : centerx]

sq_26 = img[centery*13 : h, centerx : centerx*4]

sq_27 = img[centery*13 : h, centerx*4 : centerx*7]

sq_28 = img[centery*13 : h, centerx*7 : centerx*10]

sq_29 = img[centery*13 : h, centerx*10 : centerx*13]

sq_30 = img[centery*13 : h, centerx*13 : w]

cv2.imshow("image", sq_2)

cv2.waitKey(0)

cv2.destroyAllWindows()