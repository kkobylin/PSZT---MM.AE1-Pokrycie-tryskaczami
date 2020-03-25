import Member
import IntersectArea
from math import ceil


# (1 + 1) Algorithm
def alg(width, height, radius, min_eff, prec):
    # todo ten wzor mozna przemyslec
    def rate_calculate(area, number):
        return area / (number * width * height)

    x = Member.Member(width, height, radius)
    m = 10
    c1 = 0.82
    c2 = 1.2
    # Number of chose y in the last m iterations
    fi = 0
    # Efficiency of current x
    eff = 0
    # Number of iterations
    i = 0
    # todo dobrac sigme
    sigma = 1
    # todo tez cholera wie ile min ma miec
    sigma_min = 0
    # how good solution is

    # Warunki petli zeby nie wyrzucil milion kolek z 1 iteracji
    while eff < min_eff or x.number > ceil((width + height) / radius):
        i = i + 1
        # todo Generowanie potomka y = x + sigmaE
        y = Member.Member(width, height, radius)
        x_area = IntersectArea.area_scan(prec, x.circles.copy(), y_max=height, x_max=width)
        y_area = IntersectArea.area_scan(prec, y.circles.copy(), y_max=height, x_max=width)
        x_rate = rate_calculate(x_area, x.number)
        y_rate = rate_calculate(y_area, y.number)
        if y_rate > x_rate:
            fi = fi + 1
            x = y
            eff = y_area / (width * height) * 100
        else:
            eff = x_area / (width * height) * 100

        if i % m == 0:
            if fi / m < 0.2:
                sigma = sigma * c1
            elif fi / m > 0.2:
                sigma = sigma * c2

        if sigma < sigma_min or i > 500:
            break

    print(i)
    return x, eff
