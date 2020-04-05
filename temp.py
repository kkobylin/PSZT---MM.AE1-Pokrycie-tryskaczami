import re
import numpy as np
import numpy.random as random
from numpy.random import randint
import IntersectArea
import time

from Element import Element


def main():
    matrix = np.zeros((4, 4), dtype=Element)
    x_min = 3
    x_max = 5
    y_min = 0
    y_max = 2
    forbidden_width = 2 - 1
    forbidden_height = 2 - 1
    # # matrix[x_min: x_min + forbidden_width][y_min: y_min + forbidden_height] = MatrixElement.Forbidden
    matrix[x_min: x_min + forbidden_width, y_min: y_min + forbidden_height] = Element.Forbidden
    # matrix2 = np.zeros((4, 4), dtype=Element)
    # matrix2 = matrix.copy()
    # matrix[0, 0] = Element.Taken
    # matrix2[1, 1] = Element.Taken
    nr = np.count(matrix == Element.Forbidden)
    print(nr)
    # arr = np.array([[-1, 2, 0, 4],
    #                 [4, -0.5, 6, 0],
    #                 [2.6, 0, 7, 8],
    #                 [3, -7, 4, 2.0]])
    # print("Normal array\n", arr)
    # temp = arr[0:4, 0:4]
    # print("Array with first 2 rows and alternate"
    #       "columns(0 and 2):\n", temp)
    # temp2 = matrix[0:2, 0:2]
    # print("Array with first 2 rows and alternate"
    #       "columns(0 and 2):\n", temp2)

    # width = 3
    # height = 3
    # circs = [(1, 1, 1), (1, 2, 1), (2, 1, 1), (2, 2, 1)]
    # start1 = time.perf_counter()
    # area1 = IntersectArea.area_scan(1e-1, circs, width, height)
    # stop1 = time.perf_counter()
    # start2 = time.perf_counter()
    # area2 = IntersectArea.area_scan(1e-2, circs, width, height)
    # stop2 = time.perf_counter()
    # start3 = time.perf_counter()
    # area3 = IntersectArea.area_scan(1e-3, circs, width, height)
    # stop3 = time.perf_counter()
    # start4 = time.perf_counter()
    # area4 = IntersectArea.area_scan(1e-4, circs, width, height)
    # stop4 = time.perf_counter()
    # start5 = time.perf_counter()
    # area5 = IntersectArea.area_scan(1e-5, circs, width, height)
    # stop5 = time.perf_counter()
    #
    # print("Scan1  coverage:" + str(area1 / width*height) + " time: " + str(stop1 - start1))
    # print("Scan2  coverage:" + str(area2 / width*height) + " time: " + str(stop2 - start2))
    # print("Scan3  coverage:" + str(area3 / width*height) + " time: " + str(stop3 - start3))
    # print("Scan4  coverage:" + str(area4 / width*height) + " time: " + str(stop4 - start4))
    # print("Scan5  coverage:" + str(area5 / width * height) + " time: " + str(stop5 - start5))


main()