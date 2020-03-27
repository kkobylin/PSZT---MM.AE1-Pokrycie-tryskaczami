import re
import numpy as np
import numpy.random as random
from numpy.random import randint
import IntersectArea


def main():
    f = np.ones((5, 5), dtype=bool)
    f[0][0] = False
    f[0][1] = True
    f[0][2] = True
    f[1][0] = True
    f[2][1] = False
    f[1][2] = True
    f[2][0] = True
    f[4][3] = False
    a = np.where(f == False)
    punkt_x = 6
    punkt_y = 1
    tablica = []
    for i in range(a[0].__len__()):
        odl = (a[0][i] - punkt_x)**2 + (a[1][i] - punkt_y)**2
        tablica.append(odl)

    print(np.argmin(tablica))


    # print("len = " + str(a.__len__()))
    # mem = Member.Member(4, 4, 1)
    # mem2 = Member.Member(4, 4, 1, False)
    # norm = random.normal(-0.5, 1)
    # mem2.mutate(mem, norm)
    # print(norm)
    # print(mem.circles)
    # print(mem2.circles)
    # circs = [(1, 1, 1), (2, 1, 1), (3, 1, 1), (4, 1, 1), (5, 1, 1),(6, 1, 1),(7, 1, 1),(8, 1, 1),(9, 1, 1),(10, 1, 1),(11, 1, 1),(12, 1, 1),(13, 1, 1)]
    # area = IntersectArea.area_scan(1e-3,circs, 2, 14)
    # percent = area/28 * 100
    # formatted_percent = "{:.3f}".format(percent)
    # print("Pokrycie tryskaczy wynosi " + formatted_percent + "%")

main()