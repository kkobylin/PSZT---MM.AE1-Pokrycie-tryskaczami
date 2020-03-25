import numpy as np
from numpy.random import randint


class Member:
    number = None
    radius = 1
    max_x = 1
    max_y = 1
    circles = []
    fill_matrix = None
    cover_per = None

    def __init__(self, max_x, max_y, radius):
        self.max_x = max_x
        self.max_y = max_y
        self.radius = radius
        self.fill_matrix = np.zeros((max_x - 1, max_y - 1), dtype=bool)
        pts_nr = (max_x - 1) * (max_y - 1)
        # randint(a, b) - random between <a, b)
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
