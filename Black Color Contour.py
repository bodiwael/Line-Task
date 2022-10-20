import cv2
import numpy as np

# read image as grayscale
img = cv2.imread("/home/abdelrahman/line.jpeg")

# threshold on red color
lowcolor = (0,0,0)
highcolor = (50,50,135)
thresh = cv2.inRange(img, lowcolor, highcolor)


# apply morphology close
kernel = np.ones((5,5), np.uint8)
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# get contours and filter on area
result = img.copy()
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
result = img.copy()
for c in contours:
    area = cv2.contourArea(c)
    if area > 5000:
        cv2.drawContours(result, [c], -1, (0, 255, 0), 2)


# show thresh and result    
cv2.imshow("thresh", thresh)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save resulting images
cv2.imwrite('red_line_thresh.png',thresh)
cv2.imwrite('red_line_extracted.png',result)