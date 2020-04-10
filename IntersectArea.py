from math import floor, ceil, sqrt
import numpy as np


def intersect_area(A, B):
    d = np.sqrt(np.square(B[0]-A[0]) - np.square(B[1]-A[1]))  # distance between circle's center
    if d < (A[2] + B[2]) and d != 0:
        a = A[2] * A[2]
        b = B[2] * B[2]

        x = (a - b + d * d) / (2 * d)
        z = x * x
        y = np.sqrt(a - z)

        if d <= np.abs(A[2] - B[2]):
            return np.pi * min(a, b)
        return a*np.arcsin((y/A[2])) + b*np.arcsin((y/B[2])) - y*(x+np.sqrt((z+b-a)))
    return 0

def void_area(circle, width, height):
    x = circle[0]
    y = circle[1]
    r = circle[2]
    if not (not (x + r > width and y + r > height) and not (x - r < 0 and y + r > height) and not (
            x - r < 0 and y - r < 0) and not (x + r > width and y - r < 0)):
        if x + r > width and y + r > height:
            cos_first = (width - x) / r
            cos_second = (width - x) / np.sqrt((width - x)*(width - x) + (height - y)*(height - y))
            cos_third = (height - y) / np.sqrt((width - x)*(width - x) + (height - y)*(height - y))
            cos_fourth = (height - y) / r
            arm = np.sqrt((width - x)*(width - x) + (height - y)*(height - y))

        if x - r < 0 and y + r > height:
            cos_first = x / r
            cos_second = x / np.sqrt(x * x + (height - y) * (height - y))
            cos_third = (height - y) / np.sqrt(x * x + (height - y) * (height - y))
            cos_fourth = (height - y) / r
            arm = np.sqrt(x * x + (height - y) * (height - y))

        if x - r < 0 and y - r < 0:
            cos_first = x / r
            cos_second = x / np.sqrt(x * x + y * y)
            cos_third = y / np.sqrt(x * x + y * y)
            cos_fourth = y / r
            arm = np.sqrt(x * x + y * y)

        if x + r > width and y - r < 0:
            cos_first = (width - x) / r
            cos_second = (width - x) / np.sqrt((width - x) * (width - x) + y * y)
            cos_third = y / np.sqrt((width - x) * (width - x) + y * y)
            cos_fourth = y / r
            arm = np.sqrt((width - x) * (width - x) + y * y)

        angle_first = np.arccos(cos_first) + np.arccos(cos_second)
        angle_second = np.arccos(cos_third) + np.arccos(cos_fourth)
        slice_first = angle_first / (2*np.pi) * r * r
        triangle_first = r * arm * np.sin(angle_first) / 2
        void_first = slice_first - triangle_first

        slice_second = angle_second / (2 * np.pi) * r * r
        triangle_second = r * arm * np.sin(angle_second) / 2
        void_second = slice_second - triangle_second

        void = void_first + void_second
        return void
    else:
        half_cos  = 0
        if x + r > width:
            half_cos = (width - x) / r

        if x - r < 0:
            half_cos = x / r

        if y + r > height:
            half_cos = (height - y) / r

        if y - r < 0:
            half_cos = y / r

        angle = 2*np.arccos(half_cos)
        slice_of_circle = angle / (2*np.pi) * r * r
        triangle = r * r * np.sin(angle) / 2
        void = slice_of_circle - triangle
        return void


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
