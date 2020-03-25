from math import floor, ceil, sqrt


def area_scan(prec, circs, y_max, x_max):
    # circle(cx, cy, r)
    # Zwracamy zakresy x z tym dr
    def sect(cx, cy, r, y):
        # Jakis wzorek
        dr = sqrt(r ** 2 - (y - cy) ** 2)
        return cx - dr, cx + dr

    # Lista zakresow maksymalnych podanych kolek, na osi Y
    ys = [a[1] + a[2] for a in circs] + [a[1] - a[2] for a in circs]

    # Minimalne y i maksymalne sięgniete przez zakres tryskacza
    mins = int(floor(min(ys) / prec))
    maxs = int(ceil(max(ys) / prec))

    # Total zakres w x wszystkich kol
    total = 0
    # Po osi Y wszystkie y od mins do maxs z krokiem co prec
    for y in (prec * x for x in range(mins, maxs + 1)):
        if 0 <= y <= y_max:
            # Maksymalny x na prawo
            right = -float("inf")

            # Dla kolek dla ktorych |y - cy| < r, robimy sect i dla kazdej pary (x0, x1) robimy:
            for (x0, x1) in sorted(sect(cx, cy, r, y)
                                   for (cx, cy, r) in circs
                                   if abs(y - cy) < r):
                # Ograniczenie na wielkosc pola
                if x0 < 0 + prec:
                    x0 = 0 + prec
                if x1 > x_max - prec:
                    x1 = x_max - prec

                if x1 <= right:
                    continue
                # Tutaj zliczanie pokrycia - dla kazdego y zakresy kol na osi X?
                total += x1 - max(x0, right)
                right = x1

    return total * prec
