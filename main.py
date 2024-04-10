from ColorDetectorClass import ColorDetector
from ShapeDetectorClass import ShapeDetector
import cv2
import numpy as np
import imutils

image = cv2.imread('image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 225, 255,
                       cv2.THRESH_BINARY_INV)[1]

cv2.imshow('Before', thresh)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()
cd = ColorDetector()
cv2.putText(image, 'Meller Artem 1142', (800, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
cv2.putText(image, f'{len(cnts)} contours was found!', (800, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
cd.detect_color(image)

print('Меллер Артём - 1142')
print(f'Было найдено: {len(cnts)} контуров.')
print('-' * 50)
for c in cnts:
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]))
    cY = int((M["m01"] / M["m00"]))
    shape = sd.detect(c)
    area = cv2.contourArea(c)
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(image, shape, (cX, cY),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 0), 2)
    cv2.putText(image, 'Area: ' + str(area), (cX, cY + 25),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 0), 2)

for figure_type, count in sd.get_figures_count().items():
    print(f'{figure_type}: {count}')
# show the output image
cv2.imshow("Output Image", image)
cv2.waitKey(0)
