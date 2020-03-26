import re
import EvolutionaryAlgorithm


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

    precision = 1e-3

    (m, percent) = EvolutionaryAlgorithm.alg(x, y, r, eff, precision)
    m.print_circles()

    # todo Na razie blad okolo 0.004 nawet jesli pokrywa cale pole
    formatted_percent = "{:.3f}".format(percent)
    print("Pokrycie tryskaczy wynosi " + formatted_percent + "%")
    print("Ilosc tryskaczy = " + str(m.circles.__len__()))


if __name__ == "__main__":
    main()
