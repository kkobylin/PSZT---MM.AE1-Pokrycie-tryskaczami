import re
import numpy as np
import IntersectArea


def load_params():
    input = open("input.txt", "r")  # otwieranie pliku
    params = input.readlines()  # wczytanie paramertów wejściowych
    for i in range(0, 4):
        params[i] = re.sub('[a-zA-z" "="\n"]', '',
                           params[i])  # usuwanie liter a-z, A-Z, spacji i równości, aby zosta ły liczby
    input.close();
    return params


# Raczej bedziemy trzymac w Liscie kolek (List of Tuples)
def create_matrix(x, y):
    return np.ones((x - 1, y - 1), dtype=np.int32)


def main():
    params = load_params()
    x = int(params[0])
    y = int(params[1])
    r = int(params[2])
    eff = int(params[3])
    # precision
    prec = 1e-3

    # Miejsce na dzialanie algorytmu
    circles = [
        (1, 3, 2),
        (4, 2, 4),
        (1, 1, 2)
    ]
    # todo Na razie blad okolo 0.004 nawet jesli pokrywa cale pole
    whole_area = IntersectArea.area_scan(prec, circles, y_max=y, x_max=x)
    percent = whole_area/(x*y)*100
    formatted_percent = "{:.3f}".format(percent)
    print("Pokrycie tryskaczy wynosi " + formatted_percent + "%")
    print("Rozstawienie tryskaczy: \n" + "[x,y]")
    for c in circles:
        print(str(c[1]) + "," + str(c[2]))


if __name__ == "__main__":
    main()
