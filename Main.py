import re
import EvolutionaryAlgorithm
import time
import IntersectArea


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
    radius = int(params[2])
    min_coverage = int(params[3])
    rest_areas = eval("[%s]" % params[4])  # restriction areas
    if width < 2 or height < 2 or radius < 1 or min_coverage < 0 or min_coverage > 100:
        raise Exception("Wrong arguments exception")

    # todo poprawnosc rest area
    # for (x_min, x_max, y_min, y_max) in rest_areas:
    #     print(x_min)
    #     print(x_max)

    circles = [(2, 2, 2), (2, 4, 2), (4, 2, 2), (4, 4, 2)]
    area = IntersectArea.area_scan(1e-3, circles, 6, 6, [(2, 4, 2, 4)])
    area2 = IntersectArea.area_scan(1e-3, circles, 6, 6, [])
    print(area)
    print(area2)
    # precision = 1e-2  # to calculate intersect area
    #
    # start = time.perf_counter()
    # (member, percent) = EvolutionaryAlgorithm.alg(width, height, radius, min_coverage, precision)
    # stop = time.perf_counter()
    # member.print_circles()
    #
    # formatted_percent = "{:.3f}".format(percent)
    # print("Pokrycie tryskaczy wynosi " + formatted_percent + "%")
    # print("Ilosc tryskaczy = " + str(member.circles.__len__()))
    # print("Czas : " + str(stop - start))


if __name__ == "__main__":
    main()
