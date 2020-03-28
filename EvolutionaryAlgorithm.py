import Member
import IntersectArea
from math import ceil, sqrt
import numpy.random as random


# (1 + 1) Algorithm
def alg(width, height, radius, min_eff, prec):

    def rate_calculate(area, number):
        proc = area / (width * height) * 100
        if proc >= min_eff:
            return 1/number
        else:
            return (proc - min_eff) * number**(1/3)

    x = Member.Member(width, height, radius)
    # todo Jesli nie znajduje optymalnego to mozna zwiekszyc m
    m = 20
    c1 = 0.82
    c2 = 1.2
    # Number of chose y in the last m iterations
    fi = 0
    # Efficiency of current x <0, 100>
    eff = 0
    # Number of iterations
    i = 0
    # todo dobrac sigme
    sigma = min(width, height)/(radius**2) * 2
    # todo tez cholera wie ile min ma miec
    # 1e-4 - bardzo dlugo ale wynik w miare spoko
    # 1e-3 - w miare spoko
    sigma_min = 1e-3
    # Whether calc x_area - do not have to if x didnt change
    x_changed = True
    mutate_circles = True

    while eff < min_eff or sigma > sigma_min:
        i = i + 1
        norm = random.normal(0, sigma)
        y = Member.Member(width, height, radius, False)
        y.mutate(x, norm, mutate_circles)
        if x_changed:
            x_area = IntersectArea.area_scan(prec, x.circles.copy(), width, height)
        y_area = IntersectArea.area_scan(prec, y.circles.copy(), width, height)
        x_rate = rate_calculate(x_area, x.number)
        y_rate = rate_calculate(y_area, y.number)
        if y_rate > x_rate:
            fi = fi + 1
            x = y
            x_changed = True
            eff = y_area / (width * height) * 100
        else:
            eff = x_area / (width * height) * 100
            x_changed = False

        if i % m == 0:
            if fi / m < 0.2:
                sigma = sigma * c1
                # if eff >= min_eff:
                #     mutate_circles = False
            elif fi / m > 0.2:
                sigma = sigma * c2
            fi = 0

        print("iteration = " + str(i) +  ":  eff = " + str(eff) + ", sprinklers = " + str(x.number))

        if i > 1000:
            print("Too much iterations")
            break

    print(i)
    return x, eff


# Another algorithm

