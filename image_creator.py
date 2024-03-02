from math import sqrt

import cv2
import numpy as np

# Create a white image
image = np.ones((1000, 1100, 3), dtype=np.uint8) * 255

# Draw shapes
cv2.circle(image, (600, 100), 50, (255, 0, 0), -1)  # Circle (blue)

trapezoid_coords = np.array([[(100, 100), (50, 150), (200, 150), (150, 100)]], dtype=np.int32)
cv2.fillPoly(image, [trapezoid_coords], color=(255, 255, 0))

trapezoid2_coords = np.array([[(250, 200), (150, 200), (150, 500), (250, 300)]], dtype=np.int32)
cv2.fillPoly(image, [trapezoid2_coords], color=(100, 200, 155))

# Draw the square on the image
cv2.rectangle(image, (500, 500), (550, 550), color=(200, 155, 240), thickness=-1)
cv2.rectangle(image, (700, 700), (880, 850), color=(210, 50, 100), thickness=-1)
cv2.rectangle(image, (950, 820), (910, 950), color=(100, 55, 45), thickness=-1)

parallelogram_coords = np.array([[(400, 400), (450, 300), (550, 300), (500, 400)]], dtype=np.int32)
cv2.fillPoly(image, [parallelogram_coords], color=(0, 55, 55))

rhombus_coords = np.array([[(10, 40), (40, 0), (70, 40), (40, 80)]], dtype=np.int32)
cv2.fillPoly(image, [rhombus_coords], color=(231, 155, 211))

triangle1_coords = np.array([[(500, 700), (500, 600), (550, 600)]], dtype=np.int32)
cv2.fillPoly(image, [triangle1_coords], color=(255, 205, 0))

triangle2_coords = np.array([[(300, 700), (350, 600), (350, 480)]], dtype=np.int32)
cv2.fillPoly(image, [triangle2_coords], color=(205, 255, 20))

triangle3_coords = np.array([[(230, 710), (150, 710), (150, 790)]], dtype=np.int32)
cv2.fillPoly(image, [triangle3_coords], color=(156, 2, 100))

triangle4_coords = np.array([[[400, 200], [500, 200], [450, 113]]], dtype=np.int32)
cv2.fillPoly(image, [triangle4_coords], color=(0, 255, 0))
# Save the image
cv2.imwrite("image.jpg", image)
