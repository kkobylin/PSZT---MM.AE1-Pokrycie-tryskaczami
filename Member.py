import numpy as np
from numpy.random import randint


class Member:
    radius = None
    max_x = None
    max_y = None

    def __init__(self, max_x, max_y, radius):
        self.max_x = max_x
        self.max_y = max_y
        self.radius = radius
        self.circles = []
        self.fill_matrix = np.zeros((max_x - 1, max_y - 1), dtype=bool)
        pts_nr = (max_x - 1) * (max_y - 1)
        # randint(a, b) - random between <a, b)
        # todo moze jednak nie losowac pierwszej liczby tryskaczy tylko zaczynac od wyliczonej nr = x*y/(pi*r^2)?
        self.number = randint(1, pts_nr + 1)

        for i in range(self.number):
            x = randint(1, max_x)
            y = randint(1, max_y)
            # Matrix enumerate from 0, (x, y) - coordinates on the field
            while self.fill_matrix[x - 1, y - 1]:
                x = randint(1, max_x)
                y = randint(1, max_y)
            self.fill_matrix[x - 1, y - 1] = True
            self.circles.append((x, y, radius))

    def print_circles(self):
        for c in self.circles:
            print("circle" + str(c) + ";")

    #todo konstruktor kopiujacy madry
