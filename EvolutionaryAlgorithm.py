import Member
import IntersectArea
import numpy.random as random
import numpy as np
import copy


# (1 + 1) Algorithm
def alg(width, height, radius, min_coverage, precision):

    def objective_function(area, number, iteration):
        current_coverage = area / (width * height) * 100
        # if current_coverage >= min_coverage:
            # return 1/number
        return -abs(area - np.pi*radius*radius*number) - abs(min_coverage-current_coverage)*(width * height) # * current_coverage**(1/3)/number**2
        # else:
             # return (current_coverage - min_coverage)*number ** (1/3)
        #(current_coverage - min_coverage)*number **(3)

    x = Member.Member(width, height, radius)  # First member
    # Parameters declarations
    m = 20
    c1 = 0.82  # 0.82
    c2 = 1.2  # 1.2
    fi = 0  # Number of chose y in the last m iterations
    coverage = 0  # Coverage of current x <0, 100>
    i = 0  # Number of iterations
    sigma = 5
    sigma_min = 0.1
    x_changed = True  # Whether calc x_area - do not have to if x didn't change

    while coverage < min_coverage or sigma > sigma_min:
        i = i + 1
        norm = sigma* random.normal(0, 1)
        #y = Member.Member(width, height, radius, False)
        y = copy.deepcopy(x)
        y.mutate(norm)
        if x_changed:
            x_area = IntersectArea.area_scan(precision, x.circles.copy(), width, height)
        y_area = IntersectArea.area_scan(precision, y.circles.copy(), width, height)
        x_rate = objective_function(x_area, x.number, i)
        y_rate = objective_function(y_area, y.number, i)
        if y_rate > x_rate:
            fi = fi + 1
            x = y
            x_changed = True
            coverage = y_area / (width * height) * 100
        else:
            coverage = x_area / (width * height) * 100
            x_changed = False

        if i % m == 0:
            if fi / m < 0.2:
                sigma = sigma * c1
            elif fi / m > 0.2:
                sigma = sigma * c2
            fi = 0

        print("iteration = " + str(i) +  ":  coverage = " + str(coverage) + ", sprinklers = " + str(x.number) +
              ", norm = " + str(norm) + ", sigma = " + str(sigma))

        if i > 1000:
            print("Too much iterations")
            break
    return x, coverage
