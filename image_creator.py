from math import sqrt

import cv2
import numpy as np

# Create a white image
image = np.ones((1000, 1000, 3), dtype=np.uint8) * 255

# Draw shapes
# cv2.circle(image, (100, 100), 50, (255, 0, 0), -1)  # Circle (blue)
# cv2.rectangle(image, (150, 250), (180, 200), (0, 255, 0), -1)  # Rectangle (green)
trapezoid_coords = np.array([[(100, 100), (50, 150), (200, 150), (150, 100)]], dtype=np.int32)
cv2.polylines(image, [trapezoid_coords], isClosed=True, color=(0, 255, 0), thickness=2)

trapezoid2_coords = np.array([[(250, 200), (150, 200), (150, 500), (250, 300)]], dtype=np.int32)
cv2.polylines(image, [trapezoid2_coords], isClosed=True, color=(0, 255, 0), thickness=2)

x, y = 400, 400
# Draw the square on the image
cv2.rectangle(image, (500, 500), (550, 550), color=(0, 255, 0), thickness=2)
cv2.rectangle(image, (700, 700), (880, 850), color=(0, 255, 0), thickness=2)
cv2.rectangle(image, (950, 820), (910, 950), color=(0, 255, 0), thickness=2)

parallelogram_coords = np.array([[(400, 400), (450, 300), (550, 300), (500, 400)]], dtype=np.int32)
cv2.polylines(image, [parallelogram_coords], isClosed=True, color=(0, 255, 0), thickness=2)

rhombus_coords = np.array([[(10, 40), (40, 0), (70, 40), (40, 80)]], dtype=np.int32)
cv2.polylines(image, [rhombus_coords], isClosed=True, color=(0, 255, 0), thickness=2)

triangle1_coords = np.array([[(500, 700), (500, 600), (550, 600)]], dtype=np.int32)
cv2.polylines(image, [triangle1_coords], isClosed=True, color=(0, 255, 0), thickness=2)

triangle2_coords = np.array([[(300, 700), (350, 600), (350, 480)]], dtype=np.int32)
cv2.polylines(image, [triangle2_coords], isClosed=True, color=(0, 255, 0), thickness=2)

triangle3_coords = np.array([[(230, 710), (150, 710), (150, 790)]], dtype=np.int32)
cv2.polylines(image, [triangle3_coords], isClosed=True, color=(0, 255, 0), thickness=2)

triangle4_coords = np.array([[[400, 200], [500, 200], [450, 113]]], dtype = np.int32)
cv2.polylines(image, [triangle4_coords], isClosed=True, color=(0, 255, 0), thickness=2)
# Save the image
cv2.imwrite("image.jpg", image)
