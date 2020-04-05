from math import floor, ceil, sqrt


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
                                   if abs(y - cy) < r): # tylko te kolka ktore siegaja do danego y
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
