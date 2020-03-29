from math import floor, ceil, sqrt


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
