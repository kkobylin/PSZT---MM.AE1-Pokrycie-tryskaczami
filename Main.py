import re
import EvolutionaryAlgorithm
import time
import IntersectArea
import numpy as np
from Element import Element
from Member import Member


def load_params():
    input = open("input.txt", "r")
    params = input.readlines()
    for i in range(0, 5):
        params[i] = re.sub('[a-zA-z" "="\n"_;]', '',
                           params[i])  # delete  a-z, A-Z, space i equal sign, just left numbers
    input.close()
    return params


def main():
    params = load_params()
    width = int(params[0])
    height = int(params[1])
    # todo moze radius jako double?
    radius = float(params[2])
    min_coverage = int(params[3])
    rest_areas = eval("[%s]" % params[4])  # restriction areas
    if width < 2 or height < 2 or radius < 1 or min_coverage < 0 or min_coverage > 100:
        raise Exception("Wrong arguments")

    for (x_min, x_max, y_min, y_max) in rest_areas:
        if not (isinstance(x_min, int) and isinstance(x_max, int) and isinstance(y_min, int) and isinstance(y_max, int)):
            raise Exception("Input arguments should be integers")
        if x_min >= x_max or y_min >= y_max:
            raise Exception("Wrong rest_area arguments")
        if x_max > width or x_min < 0 or y_max > height or y_min < 0:
            raise Exception("Wrong rest_area arguments")

    Member.height = height
    Member.width = width
    Member.radius = radius
    Member.set_restricted_areas(rest_areas)

    precision = 1e-2  # to calculate intersect area
    start = time.perf_counter()
    (member, percent) = EvolutionaryAlgorithm.alg(width, height, radius, min_coverage, precision, rest_areas)
    stop = time.perf_counter()
    member.print_circles()

    formatted_percent = "{:.3f}".format(percent)
    print("Pokrycie tryskaczy wynosi " + formatted_percent + "%")
    print("Ilosc tryskaczy = " + str(member.circles.__len__()))
    print("Czas : " + str(stop - start))


if __name__ == "__main__":
    main()
