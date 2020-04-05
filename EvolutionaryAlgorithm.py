import Member
import IntersectArea
import numpy.random as random
import numpy as np


# (1 + 1) Algorithm
def alg(width, height, radius, min_coverage, precision, rest_areas):
    restricted = np.full((width, height), 0, dtype=int)
    for (x_min, x_max, y_min, y_max) in rest_areas:
        restricted[x_min: x_max, y_min: y_max] = 1
    restricted_area = np.sum(restricted)
    del restricted
    whole_area = width * height - restricted_area

    def objective_function(area, number):
        current_coverage = area / whole_area * 100
        if current_coverage >= min_coverage:
            return 1/number * current_coverage ** (1 / 4)
        else:
            return (current_coverage - min_coverage) * number ** (1 / 3)

    x = Member.Member()  # First member
    # Parameters declarations
    m = 10
    c1 = 0.82
    c2 = 1.2
    fi = 0  # Number of chose y in the last m iterations
    coverage = 0  # Coverage of current x <0, 100>
    i = 0  # Number of iterations
    sigma = min(width, height)/(radius**2) * 2
    sigma_min = 1e-3
    x_changed = True  # Whether calc x_area - do not have to if x didn't change

    while coverage < min_coverage or sigma > sigma_min:
        i = i + 1
        norm = random.normal(0, sigma)
        y = Member.Member(False)
        y.mutate(x, norm)
        if x_changed:
            x_area = IntersectArea.area_scan(precision, x.circles.copy(), width, height, rest_areas)
        y_area = IntersectArea.area_scan(precision, y.circles.copy(), width, height, rest_areas)
        x_rate = objective_function(x_area, x.number)
        y_rate = objective_function(y_area, y.number)
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

        print("iteration = " + str(i) +  ":  coverage = " + str(coverage) + ", sprinklers = " + str(x.number))

        if i > 1000:
            print("Too much iterations")
            break
    return x, coverage
