from math import floor, ceil, sqrt
import numpy as np


def intersect_area(first, second):
    d = np.sqrt((second[0] - first[0]) * (second[0] - first[0]) + (second[1] - first[1]) * (second[1] - first[1]))
    if d < (first[2] + second[2]) and d != 0:
        a = first[2] * first[2]
        b = second[2] * second[2]

        x = (a - b + d * d) / (2 * d)
        z = x * x
        y = np.sqrt(a - z)

        if d <= np.abs(first[2] - second[2]):
            return np.pi * min(a, b)
        return a * np.arcsin((y / first[2])) + b * np.arcsin((y / second[2])) - y * (x + np.sqrt((z + b - a)))
    return 0


def void_area(circle, width, height, rest_areas):
    void = 0
    x = circle[0]
    y = circle[1]
    r = circle[2]
    # dla kółek na rogach
    if (x + r > width and y + r > height) or (x - r < 0 and y + r > height) or (x - r < 0 and y - r < 0) \
            or (x + r > width and y - r < 0):
        cos_first = cos_second = cos_third = cos_fourth = arm = 0
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
        slice_first = angle_first / 2 * r * r
        triangle_first = r * arm * np.sin(angle_first) / 2
        void_first = slice_first - triangle_first

        slice_second = angle_second / 2 * r * r
        triangle_second = r * arm * np.sin(angle_second) / 2
        void_second = slice_second - triangle_second

        void = void_first + void_second
    else:
        # dla kółek na brzegach
        if x + r > width or x - r < 0 or y + r > height or y - r < 0:
            half_cos = 0
            if x + r > width:
                half_cos = (width - x) / r

            if x - r < 0:
                half_cos = x / r

            if y + r > height:
                half_cos = (height - y) / r

            if y - r < 0:
                half_cos = y / r

            angle = 2*np.arccos(half_cos)
            slice_of_circle = angle / 2 * r * r
            triangle = r * r * np.sin(angle) / 2
            void = slice_of_circle - triangle
    for (x_min, x_max, y_min, y_max) in rest_areas:
        void = void + circle_rectangle_intersection_area(x-1, y-1, r, x_min, x_max, y_min, y_max)
    return void


# Finds the area of the intersection between a circle and a rectangle
# http://stackoverflow.com/questions/622287/area-of-intersection-between-circle-and-rectangle
def circle_rectangle_intersection_area(x_center, y_center, r, x_left, x_right, y_bottom, y_top):
    # find the signed (negative out) normalized distance from the circle center to each of the infinitely extended
    # rectangle edge lines,
    d = [0, 0, 0, 0]
    d[0] = (x_center - x_left) / r
    d[1] = (y_center - y_bottom) / r
    d[2] = (x_right - x_center) / r
    d[3] = (y_top - y_center) / r
    # for convenience order 0,1,2,3 around the edge.

    # To begin, area is full circle
    area = np.pi * r * r

    # Check if circle is completely outside rectangle, or a full circle
    full = True
    for d_i in d:
        if d_i <= -1:  # Corresponds to a circle completely out of bounds
            return 0
        if d_i < 1:  # Corresponds to the circular segment out of bounds
            full = False

    if full:
        return area

    # this leave only one remaining fully outside case: circle center in an external quadrant, and distance to corner
    # greater than circle radius: for each adjacent i,j
    adj_quads = [1, 2, 3, 0]
    for i in [0, 1, 2, 3]:
        j = adj_quads[i]
        if d[i] <= 0 and d[j] <= 0 and d[i] * d[i] + d[j] * d[j] > 1:
            return 0

    # now begin with full circle area  and subtract any areas in the four external half planes
    a = [0, 0, 0, 0]
    for d_i in d:
        if -1 < d_i < 1:
            a[i] = np.arcsin(d_i)  # save a_i for next step
            area -= 0.5 * r * r * (np.pi - 2 * a[i] - np.sin(2 * a[i]))

            # At this point note we have double counted areas in the four external quadrants, so add back in:
    # for each adjacent i,j

    for i in [0, 1, 2, 3]:
        j = adj_quads[i]
        if d[i] < 1 and d[j] < 1 and d[i] * d[i] + d[j] * d[j] < 1:
            # The formula for the area of a circle contained in a plane quadrant is readily derived as the sum of a
            # circular segment, two right triangles and a rectangle.
            area += 0.25 * r * r * (
                        np.pi - 2 * a[i] - 2 * a[j] - np.sin(2 * a[i]) - np.sin(2 * a[j]) + 4 * np.sin(
                    a[i]) * np.sin(a[j]))
    return area


def area_scan(precision, circles, width, height, rest_areas):
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

            for (x0, x1) in sorted(sect(cx, cy, r, y)   # liczymy zasieg x0-x1 dla danego y dla kazdego kolka
                                   for (cx, cy, r) in circles
                                   if abs(y - cy) < r):  # tylko te kolka ktore siegaja do danego y
                if x0 < 0:
                    x0 = 0
                if x1 > width:
                    x1 = width
                if x1 <= right:
                    continue

                # Do not add restricted areas
                continue_flag = False  # do not add this section to score, because of restricted area
                obstacle_section = 0  # section to subtract from score
                for (x_min, x_max, y_min, y_max) in rest_areas:
                    if y_min <= y <= y_max:
                        # 4 przypadki:
                        # 1: x0 wchodzi na restricted area
                        # 2: x1 wchodzi na restricted area
                        # 3: restricted area zawiera sie pomiedzy x0 i x1
                        # 4: x0 i x1 zawiera sie w restricted area
                        if x0 >= x_min and x1 <= x_max:  # 4
                            continue_flag = True
                            break
                        elif x_min >= x0 and x_max <= x1:  # 3
                            # todo moze byc wiele restricted area w ramach jednego kolka
                            obstacle_section += (x_max - x_min)
                        elif x_min <= x1 <= x_max:  # 2
                            x1 = x_min
                        elif x_min <= x0 <= x_max:  # 1
                            x0 = x_max
                if continue_flag:
                    continue
                total -= obstacle_section

                total += x1 - max(x0, right)
                right = x1

    return total * precision
