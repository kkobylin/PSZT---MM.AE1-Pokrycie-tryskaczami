import re
import numpy as np
import numpy.random as random
from numpy.random import randint
import IntersectArea
import time
from scipy.ndimage import measurements
from scipy import ndimage

from Element import Element


def main():
    circles = [(6, 8, 1.0),
    (6, 9, 1.0),
    (5, 6, 1.0),
    (6, 4, 1.0),
    (4, 4, 1.0),
    (5, 5, 1.0),
    (3, 2, 1.0),
    (9, 7, 1.0),
    (5, 1, 1.0),
    (4, 8, 1.0),
    (1, 4, 1.0),
    (4, 3, 1.0),
    (2, 4, 1.0),
    (9, 6, 1.0),
    (7, 5, 1.0),
    (7, 2, 1.0),
    (4, 7, 1.0),
    (9, 5, 1.0),
    (7, 7, 1.0),
    (8, 9, 1.0),
    (3, 5, 1.0),
    (2, 3, 1.0),
    (3, 7, 1.0),
    (7, 8, 1.0),
    (9, 1, 1.0),
    (1, 9, 1.0),
    (6, 3, 1.0),
    (5, 9, 1.0),
    (8, 8, 1.0),
    (9, 9, 1.0),
    (3, 4, 1.0),
    (2, 6, 1.0),
    (2, 9, 1.0),
    (9, 3, 1.0),
    (9, 8, 1.0),
    (7, 6, 1.0),
    (8, 4, 1.0),
    (1, 8, 1.0),
    (3, 9, 1.0),
    (7, 9, 1.0)]

    # matrix = np.full((9, 9), Element.Empty, dtype=Element)
    matrix = np.full((9, 9), 0)
    for (x, y, r) in circles:
        matrix[x - 1, y - 1] = 1

    mm = np.flipud(matrix)
    # print(mm)
    # print(mm.sum(axis=1))
    # print(mm.sum(axis=0))
    # x = np.argmin(mm.sum(axis=1))
    # y = np.argmin(mm.sum(axis=0))
    # n = mm.copy()
    # print(x, y)
    # print(matrix[x, y])

    # print(mm)
    # print("--------------")
    # center = ndimage.measurements.center_of_mass(mm)
    # # center = ndimage.maximum_position(mm)
    # print(center)
    x = 6; y = 3
    print(circles.index((6, 8, 1)))

main()