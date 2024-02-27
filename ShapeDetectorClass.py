"""
Класс для распознования объектов на основе библиотеки OpenCV
"""
from math import sqrt

import cv2
import numpy
import numpy as np


# def determine_quadrilateral_shape(coords):
#     # Calculate the lengths of the sides
#     coords = np.around(coords, decimals=-1)
#     print(coords)
#     side_lengths = [np.linalg.norm(coords[i] - coords[(i + 1) % 4]) for i in range(4)]
#
#     # Calculate the angles between the sides
#     angles = []
#     for i in range(4):
#         v1 = coords[(i + 1) % 4] - coords[i]
#         v2 = coords[(i + 2) % 4] - coords[(i + 1) % 4]
#         angle = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
#         angles.append(np.degrees(angle))
#     print('1' if 0 in angles else '0')
#     print(side_lengths)
#     angles.remove(numpy.nan)
#     print(set(side_lengths), set(angles))
#     # Check for shape based on side lengths and angles
#     if len(set(side_lengths)) == 1 and len(set(angles)) == 1:
#         return "Square"
#     elif len(set(side_lengths)) == 2 and len(set(angles)) == 1:
#         return "Rectangle"
#     elif len(set(side_lengths)) == 4 and len(set(angles)) == 4:
#         return "Rhombus"
#     elif len(set(angles)) == 2:
#         return "Trapezoid"
#     else:
#         return "Quadrilateral"


class ShapeDetector:
    def __init__(self):
        pass



    def detect(self, c, img):

        """
        Функция для определения формы объекта
        :param c:
        :return:
        """
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        font = cv2.FONT_HERSHEY_COMPLEX
        if len(approx) == 3:
            # Если контур состоит из 3 вершин, то это треугольник
            n = approx.ravel()
            i = 0

            letters = {0: 'A', 2: 'B', 4: 'C', 6: "D"}
            cords = []
            for j in n:
                if (i % 2 == 0):
                    x = n[i]
                    y = n[i + 1]
                    cords.extend([x, y])
                    # String containing the co-ordinates.
                    string = str(letters[i]) + " " + str(x) + " " + str(y)
                    # text on remaining co-ordinates.
                    cv2.putText(img, string, (x, y), font, 0.5, (0, 0, 0))
                i = i + 1
            coords = np.around(cords, decimals=-1)
            xa, ya, xb, yb, xc, yc = coords
            side1 = sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
            side2 = sqrt((xc - xb) ** 2 + (yc - yb) ** 2)
            side3 = sqrt((xc - xa) ** 2 + (yc - ya) ** 2)
            print(side1, side2, side3)
            if (side1 < side2 + side3) and (side2 < side1 + side3) and (side3 < side1 + side2):
                if side1 == side2 == side3:
                    shape = "Equilateral triangle"
                elif side1 == side2 or side1 == side3 or side2 == side3:
                    shape = "Isosceles triangle"
                elif (side1 ** 2 + side2 ** 2 == side3 ** 2) or (side1 ** 2 + side3 ** 2 == side2 ** 2) or (
                        side2 ** 2 + side3 ** 2 == side1 ** 2):
                    shape = "Right-angled triangle"
                else:
                    shape = "Triangle"
        elif len(approx) == 4:
            # Used to flatted the array containing
            # the co-ordinates of the vertices.
            n = approx.ravel()
            i = 0

            letters = {0: 'A', 2: 'B', 4: 'C', 6: "D"}
            cords = []
            for j in n:
                if (i % 2 == 0):
                    x = n[i]
                    y = n[i + 1]
                    cords.extend([x, y])
                    # String containing the co-ordinates.
                    string = str(letters[i]) + " " + str(x) + " " + str(y)
                    # text on remaining co-ordinates.
                    cv2.putText(img, string, (x, y), font, 0.5, (0, 0, 0))
                i = i + 1
            coords = np.around(cords, decimals=-1)

            # shape = determine_quadrilateral_shape(np.array(cords))
            xa, ya, xb, yb, xc, yc, xd, yd = coords
            eps = 1e-7
            a = eps > abs((xb - xa) * (yc - yd) - (xc - xd) * (yb - ya))
            b = eps > abs((xc - xb) * (yd - ya) - (xd - xa) * (yc - yb))
            c = eps > abs(sqrt((xb - xa) ** 2 + (yb - ya) ** 2) - sqrt((xc - xb) ** 2 + (yc - yb) ** 2))
            if a or b:
                if a and b:
                    if eps > abs(sqrt((xc - xa) ** 2 + (yc - ya) ** 2) - sqrt((xd - xb) ** 2 + (yd - yb) ** 2)):
                        if c:
                            shape = 'Square'
                        else:
                            shape = 'Rectangle'
                    else:
                        if c:
                            shape = 'Rhombus'
                        else:
                            shape = 'Parallelogram'

                else:
                    shape = 'Trapezoid'

            else:
                shape = 'Quadrilateral'
        elif len(approx) == 5:
            shape = "Pentagon"
        else:
            shape = "Circle"

        # return the name of the shape
        return shape
