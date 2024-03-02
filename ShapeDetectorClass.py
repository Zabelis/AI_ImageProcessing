"""
Класс для распознования объектов на основе библиотеки OpenCV
"""
import math
from math import sqrt

import cv2
import numpy
import numpy as np


class ShapeDetector:
    def __init__(self):
        """
        Инициализация словаря
        """
        self.figures_dict = {}

    def add_new_figure(self, figure_type):
        """
        Увеличение количество фигур
        :param figure_type:
        :return:
        """
        self.figures_dict[figure_type] = self.figures_dict.get(figure_type, 0) + 1

    def get_figures_count(self):
        """
        Получение словаря с количеством фигур
        :return:
        """
        return self.figures_dict

    def detect(self, c):

        """
        Функция для определения формы объекта
        :param c:
        :return:
        """
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        if len(approx) == 3:
            # Если контур состоит из 3 вершин, то это треугольник
            xa, ya, xb, yb, xc, yc = self.get_figure_coordinates(approx)  # выделение координат точек

            side1 = sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
            side2 = sqrt((xc - xb) ** 2 + (yc - yb) ** 2)
            side3 = sqrt((xc - xa) ** 2 + (yc - ya) ** 2)
            if (side1 < side2 + side3) and (side2 < side1 + side3) and (side3 < side1 + side2):
                if abs(side1 - side2) <= 3 and abs(side2 - side3) <= 3:
                    self.add_new_figure("Equilateral triangle")
                    return "Equilateral triangle"
                elif side1 == side2 or side1 == side3 or side2 == side3:
                    self.add_new_figure("Isosceles triangle")
                    return "Isosceles triangle"
                elif (side1 ** 2 + side2 ** 2 == side3 ** 2) or (side1 ** 2 + side3 ** 2 == side2 ** 2) or (
                        side2 ** 2 + side3 ** 2 == side1 ** 2):
                    self.add_new_figure("Right-angled triangle")
                    return "Right-angled triangle"
                else:
                    self.add_new_figure("Triangle")
                    return "Triangle"
        elif len(approx) == 4:
            # Used to flatted the array containing
            # the co-ordinates of the vertices.

            xa, ya, xb, yb, xc, yc, xd, yd = self.get_figure_coordinates(approx)
            eps = 1e-7
            a = eps > abs((xb - xa) * (yc - yd) - (xc - xd) * (yb - ya))
            b = eps > abs((xc - xb) * (yd - ya) - (xd - xa) * (yc - yb))
            c = eps > abs(sqrt((xb - xa) ** 2 + (yb - ya) ** 2) - sqrt((xc - xb) ** 2 + (yc - yb) ** 2))
            if a or b:
                if a and b:
                    if eps > abs(sqrt((xc - xa) ** 2 + (yc - ya) ** 2) - sqrt((xd - xb) ** 2 + (yd - yb) ** 2)):
                        if c:
                            self.add_new_figure('Square')
                            return 'Square'
                        else:
                            self.add_new_figure('Rectangle')
                            return 'Rectangle'
                    else:
                        if c:
                            self.add_new_figure('Rhombus')
                            return 'Rhombus'
                        else:
                            self.add_new_figure('Parallelogram')
                            return 'Parallelogram'
                else:
                    self.add_new_figure('Trapezoid')
                    return 'Trapezoid'
            else:
                self.add_new_figure('Quadrilateral')
                return 'Quadrilateral'
        elif len(approx) == 5:
            self.add_new_figure("Pentagon")
            return "Pentagon"
        elif len(approx) == 6:
            self.add_new_figure("Hexagon")
            return "Hexagon"
        else:
            self.add_new_figure("Circle")
            return "Circle"

    def get_figure_coordinates(self, approx):
        """
        Получение координат фигуры
        :param approx:
        :return:
        """
        n = approx.ravel() # Получение координат

        i = 0
        cords = []
        for j in n:
            if (i % 2 == 0):
                x = n[i]
                y = n[i + 1]
                cords.extend([x, y])
            i = i + 1
        coords = np.around(cords, decimals=-1)
        return coords
