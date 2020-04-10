from typing import Dict, Any, Union

import numpy as np
from numpy.random import randint
import IntersectArea


class Member:
    radius = None
    width = None
    height = None

    def __init__(self, width, height, radius):
        self.width = width
        self.height = height
        self.radius = radius
        self.circles = []
        self.fill_matrix = np.zeros((width - 1, height - 1), dtype=bool)
        pts_nr = (width - 1) * (height - 1)
        # randint(a, b) - random between <a, b)
        #self.number = randint(round(pts_nr / 2), pts_nr + 1)  # number of sprinklers is high at start
        self.number = randint(0, pts_nr + 1)
        for i in range(self.number):
            empty_fields = np.where(self.fill_matrix == False)
            free_field = randint(0, empty_fields[0].__len__())
            # (x, y) - coordinates on the field, matrix contains (x-1)*(y-1) elements
            x = empty_fields[0][free_field] + 1
            y = empty_fields[1][free_field] + 1
            self.fill_matrix[x - 1, y - 1] = True
            self.circles.append((x, y, radius))

    def print_circles(self):
        output = open("output.txt", "w")
        for c in self.circles:
            output.write("circle" + str(c) + ";\n")
        output.close()

    def mutate(self, norm):
        mutation = self.number * norm  # mutation can be positive and negative
        # Mutate number of circles
        old_number = self.number
        self.number = round(self.number - mutation)  # change number of sprinklers
        if self.number > (self.width - 1) * (self.height - 1):
            self.number = (self.width - 1) * (self.height - 1)
        elif self.number < 1:
            self.number = 1

        # Copy circles from parent to child (child may have more circles than parent)
        # indexes_of_circles_to_copy = np.random.choice(other.number, min(self.number, other.number), replace=False)
        difference = old_number - self.number
        if difference > 0:  # have to delete some sprinklers
            mutual_area = self.calculate_mutual_area(True)
            for i in range(difference):
                circle_key = max(mutual_area, key=lambda k: mutual_area[k])
                x = circle_key[0]
                y = circle_key[1]
                r = circle_key[2]
                self.circles.remove((x, y, r))
                self.fill_matrix[x-1, y-1] = False
                del mutual_area[circle_key]
        else:  # have to add some sprinklers
            for i in range(-difference):
                mutual_area = self.calculate_mutual_area(False)
                circle_key = max(mutual_area, key=lambda k: mutual_area[k])
                x = circle_key[0]
                y = circle_key[1]
                r = circle_key[2]
                self.circles.append((x, y, r))
                self.fill_matrix[x-1, y-1] = True
        # Mutate every 5th circle
        # for i in range(0, self.number, 5):
        #     circle_to_mutate = randint(0, self.number)
        #     empty_fields = np.where(self.fill_matrix == False)
        #     if empty_fields[0].__len__() == 0:
        #         break
        #     x_old = self.circles[circle_to_mutate][0]
        #     y_old = self.circles[circle_to_mutate][1]
        #     x_or_y = randint(0, 2)  # Mutate only x or only y, not both
        #     if x_or_y:
        #         x_new = round(x_old + x_old * norm)
        #         y_new = y_old
        #         if x_new >= self.width - 1:
        #             x_new = self.width - 1
        #         elif x_new < 1:
        #             x_new = 1
        #     else:
        #         x_new = x_old
        #         y_new = round(y_old + y_old * norm)
        #         if y_new >= self.height - 1:
        #             y_new = self.height - 1
        #         elif y_new < 1:
        #             y_new = 1
        #     distance = []  # Distance from empty places - mean square
        #     for k in range(empty_fields[0].__len__()):
        #         dis = (empty_fields[0][k] - x_new) ** 2 + (empty_fields[1][k] - y_new) ** 2
        #         distance.append(dis)
        #         if dis < 1:
        #             break
        #
        #     x_new = empty_fields[0][np.argmin(distance)] + 1
        #     y_new = empty_fields[1][np.argmin(distance)] + 1
        #     # Remove circle before mutation
        #     self.fill_matrix[x_old - 1, y_old - 1] = False
        #     self.circles.remove((x_old, y_old, self.radius))
        #     # Add circle after mutation
        #     self.fill_matrix[x_new - 1, y_new - 1] = True
        #     self.circles.append((x_new, y_new, self.radius))

    def calculate_mutual_area(self, busy):
        mutual_area = {}
        area = 0
        empty_fields = np.where(self.fill_matrix == False)
        busy_fields = np.where(self.fill_matrix == True)
        if busy:
            for i in range(busy_fields[0].__len__()):  # which count
                x_i = busy_fields[0][i] + 1
                y_i = busy_fields[1][i] + 1
                for j in range(busy_fields[0].__len__()):  # comparison
                    x_j = busy_fields[0][j] + 1
                    y_j = busy_fields[1][j] + 1
                    area = area + IntersectArea.intersect_area((x_i, y_i, self.radius), (x_j, y_j, self.radius))
                mutual_area.update({(x_i, y_i, self.radius): area})
                area = 0
        else:
            for i in range(empty_fields[0].__len__()):  # which count
                x_i = empty_fields[0][i] + 1
                y_i = empty_fields[1][i] + 1
                for j in range(busy_fields[0].__len__()):  # comparison
                    x_j = busy_fields[0][j] + 1
                    y_j = busy_fields[1][j] + 1
                    area = area + IntersectArea.intersect_area((x_i, y_i, self.radius), (x_j, y_j, self.radius))
                cover_area = (np.pi * self.radius * self.radius) - IntersectArea.void_area((x_i, y_i, self.radius),
                                                                                         self.width, self.height) - area
                mutual_area.update({(x_i, y_i, self.radius): cover_area})
                area = 0
        return mutual_area

