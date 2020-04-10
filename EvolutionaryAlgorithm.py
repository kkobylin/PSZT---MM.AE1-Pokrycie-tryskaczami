import Member
import IntersectArea
import numpy.random as random
import numpy as np
import copy


# (1 + 1) Algorithm
def alg(width, height, radius, min_coverage, precision, rest_areas):
    restricted = np.full((width, height), 0, dtype=int)
    for (x_min, x_max, y_min, y_max) in rest_areas:
        restricted[x_min: x_max, y_min: y_max] = 1
    restricted_area = np.sum(restricted)
    del restricted
    whole_area = width * height - restricted_area

    def objective_function(area, number, it):
        current_coverage = area / whole_area * 100
        if current_coverage >= min_coverage:
            return 1/number * current_coverage ** (1 / 4)
        else:
            return (current_coverage - min_coverage) * number ** (1 / 3)
        # todo zapamietac najlepsze rozwiazanie z pierwszej funkcji celu
        # todo znormalizowac numer bo coverage zawsze 0 100 a numery rozne
        # if it < 250:
        #     return current_coverage / number ** (1/6)
        # # elif it < 310:
        # #     if current_coverage >= min_coverage - 5:
        # #         return 1 / number * current_coverage ** (1 / 4)
        # #     else:
        # #         return (current_coverage - min_coverage) * number ** (1 / 3)
        # else:
        #     if current_coverage >= min_coverage:
        #         return 1 / number
        #     else:
        #         return (current_coverage - min_coverage) * number ** (1 / 3)
        # return -abs(area - np.pi * radius * radius * number) / (width * height) - abs(min_coverage - current_coverage)

    x = Member.Member()  # First member
    # Parameters declarations
    m = 15
    c2 = 1.06
    c1 = 1 / c2
    fi = 0  # Number of chose y in the last m iterations
    coverage = 0  # Coverage of current x <0, 100>
    i = 0  # Number of iterations
    sigma = round(whole_area / (4 * radius))
    sigma_min = 0.1
    x_changed = True  # Whether calc x_area - do not have to if x didn't change

    while coverage < min_coverage or sigma > sigma_min:
        i = i + 1
        norm = sigma * random.normal(0, 1)
        y = Member.Member(False)
        y.mutate(x, norm, sigma)
        if x_changed:
            x_area = IntersectArea.area_scan(precision, x.circles.copy(), width, height, rest_areas)
        y_area = IntersectArea.area_scan(precision, y.circles.copy(), width, height, rest_areas)
        x_rate = objective_function(x_area, x.number, i)
        y_rate = objective_function(y_area, y.number, i)
        print("it ", i, " x_num:", x.number, " x_cov:", int(x_area / whole_area * 100), " y_num:",
              y.number, " y_cov:", int(y_area / whole_area * 100), " sigma:", sigma)
        if y_rate > x_rate:
            fi = fi + 1
            x = y
            x_changed = True
            coverage = y_area / whole_area * 100
        else:
            coverage = x_area / whole_area * 100
            x_changed = False

        if i % m == 0:
            if fi / m < 0.2:
                sigma = sigma * c1
            elif fi / m > 0.2:
                sigma = sigma * c2
            fi = 0

        if i > 2000:
            print("Too much iterations")
            break
    return x, coverage
