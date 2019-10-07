import numpy as np
import cv2

img = np.zeros([512, 512, 3], np.uint8)
#img = cv2.imread('lena.jpg', 1)
#255, 156, 8
img = cv2.line(img, (0, 0), (510, 0), (255, 255, 255), 10)
img = cv2.line(img, (510, 0), (510, 510), (255, 255, 255), 10)
img = cv2.line(img, (510, 510), (0, 510), (255, 255, 255), 10)
img = cv2.line(img, (0, 510), (0, 0), (255, 255, 255), 10)
img = cv2.circle(img, (15, 15), 8, (255, 255, 255), 10)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "Opencv", (10, 500), font, 4,
                  (255, 255, 255), 10, cv2.LINE_AA)
#img = cv2.rectangle(img, (20, 20), (490, 490), (8, 156, 255), 10)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
