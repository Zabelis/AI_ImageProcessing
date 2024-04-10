
import cv2
import numpy as np

# Get color
color = np.uint8([[[210, 50, 100]]])

# Convert color to HSV
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

# Print HSV Value for color
print(hsv)
