import re
import EvolutionaryAlgorithm
import time
import IntersectArea


def load_params():
    input = open("input.txt", "r")  # otwieranie pliku
    params = input.readlines()  # wczytanie paramertów wejściowych
    for i in range(0, 4):
        params[i] = re.sub('[a-zA-z" "="\n"]', '',
                           params[i])  # usuwanie liter a-z, A-Z, spacji i równości, aby zosta ły liczby
    input.close()
    return params


def main():
    params = load_params()
    x = int(params[0])
    y = int(params[1])
    r = int(params[2])
    eff = int(params[3])
    if x < 2 or y < 2 or r < 1 or eff < 0 or eff > 100:
        raise Exception("Wrong arguments exception")

    precision = 1e-2

    start = time.perf_counter()
    (m, percent) = EvolutionaryAlgorithm.alg(x, y, r, eff, precision)
    stop = time.perf_counter()
    m.print_circles()

    formatted_percent = "{:.3f}".format(percent)
    print("Pokrycie tryskaczy wynosi " + formatted_percent + "%")
    print("Ilosc tryskaczy = " + str(m.circles.__len__()))
    print("Czas : " + str(stop - start))
    more_precised_percent = IntersectArea.area_scan(1e-3, m.circles, x, y)/(x*y) * 100
    formatted_percent = "{:.3f}".format(more_precised_percent)
    print("Prawdziwe pokrycie = " + str(formatted_percent))


if __name__ == "__main__":
    main()
