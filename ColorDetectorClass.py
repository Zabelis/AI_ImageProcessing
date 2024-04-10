import cv2
import numpy as np

class ColorDetector:
    def detect_color(self, img):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        masks = {
            'Red1': ([0, 100, 100], [12, 255, 255]),
            'Orange': ([13, 100, 100], [23, 255, 255]),
            'Yellow': ([24, 100, 100], (35, 255, 255)),
            'Green': ([36, 100, 100], [69, 255, 255]),
            'Turquoise': ([70, 100, 100], [94, 255, 255]),
            'Blue': ([95, 100, 100], [135, 255, 255]),
            'Purple': ([136, 100, 100], [163, 255, 255]),
            'Red2': ([164, 100, 100], [180, 255, 255]),
            'Pink': ([140, 50, 50], [170, 255, 255])
        }

        for name, hsv_range in masks.items():
            lower = np.array(hsv_range[0])
            upper = np.array(hsv_range[1])
            mask = cv2.inRange(hsv, lower, upper)
            contours, i = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for cnt in contours:
                M = cv2.moments(cnt)
                area = cv2.contourArea(cnt)
                if area > 100:
                    cX = int((M["m10"] / M["m00"]))
                    cY = int((M["m01"] / M["m00"]))
                    cv2.putText(img, name, (cX, cY + 55),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (0, 0, 0), 2)

