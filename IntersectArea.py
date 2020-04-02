from math import floor, ceil, sqrt
import numpy as np


def intersect_area(A, B):
    d = np.sqrt(np.square(B[0]-A[0]) - np.square(B[1]-A[1]))  # distance between circle's center
    if d < (A[2] + B[2]):
        a = A[2] * A[2]
        b = B[2] * B[2]

        x = (a - b + d * d) / (2 * d)
        z = x * x
        y = np.sqrt(a - z)

        if d <= np.abs(A[2] - B[2]):
            return np.pi * min(a, b)
        return a*np.arcsin((y/A[2])) + b*np.arcsin((y/B[2])) - y*(x+np.sqrt((z+b-a)))
    return 0


def area_scan(precision, circles, width, height):

    def sect(cx, cy, r, y):
        dr = sqrt(r ** 2 - (y - cy) ** 2)
        return cx - dr, cx + dr

    ys = [a[1] + a[2] for a in circles] + [a[1] - a[2] for a in circles]

    mins = int(floor(min(ys) / precision))
    maxs = int(ceil(max(ys) / precision))

    total = 0
    for y in (precision * x for x in range(mins, maxs + 1)):
        if 0 <= y < height:
            right = -float("inf")

            for (x0, x1) in sorted(sect(cx, cy, r, y)
                                   for (cx, cy, r) in circles
                                   if abs(y - cy) < r):
                if x0 < 0:
                    x0 = 0
                if x1 > width:
                    x1 = width

                if x1 <= right:
                    continue
                total += x1 - max(x0, right)
                right = x1

    return total * precision
