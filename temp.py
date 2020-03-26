import re
import numpy as np
import numpy.random as random
from numpy.random import randint
import Member
import EvolutionaryAlgorithm
import IntersectArea


def main():
    # f = np.zeros((3, 3), dtype=bool)
    # f[0][0] = False
    # f[0][1] = True
    # f[0][2] = True
    # f[1][0] = True
    # f[1][1] = False
    # f[1][2] = True
    # f[2][0] = True
    # f[2][1] = True
    # f[2][2] = False
    # a = np.where(f == False)
    # print(a[1][2])
    # print(a[0][2])
    # print("len = " + str(a.__len__()))
    # mem = Member.Member(4, 4, 1)
    # mem2 = Member.Member(4, 4, 1, False)
    # norm = random.normal(-0.5, 1)
    # mem2.mutate(mem, norm)
    # print(norm)
    # print(mem.circles)
    # print(mem2.circles)
    circs = [(1, 1, 1), (3, 1, 1), (1, 3, 1), (3, 3, 1), (2, 2, 1)]
    area = IntersectArea.area_scan(1e-3,circs, 4, 4)
    percent = area/16 * 100
    formatted_percent = "{:.3f}".format(percent)
    print("Pokrycie tryskaczy wynosi " + formatted_percent + "%")

main()