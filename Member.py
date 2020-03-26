import numpy as np
from numpy.random import randint


class Member:
    radius = None
    width = None
    height = None

    def __init__(self, width, height, radius, add_circles=True):
        self.width = width
        self.height = height
        self.radius = radius
        if add_circles:
            self.circles = []
            self.fill_matrix = np.zeros((width - 1, height - 1), dtype=bool)
            pts_nr = (width - 1) * (height - 1)
            # randint(a, b) - random between <a, b)
            # todo moze jednak nie losowac pierwszej liczby tryskaczy tylko zaczynac od wyliczonej nr = x*y/(pi*r^2)?
            self.number = randint(1, pts_nr + 1)

            for i in range(self.number):
                x = randint(1, width)
                y = randint(1, height)
                # Matrix enumerate from 0, (x, y) - coordinates on the field
                while self.fill_matrix[x - 1, y - 1]:
                    x = randint(1, width)
                    y = randint(1, height)
                self.fill_matrix[x - 1, y - 1] = True
                self.circles.append((x, y, radius))

    def print_circles(self):
        for c in self.circles:
            print("circle" + str(c) + ";")

    def mutate(self, other, norm):
        self.circles = []
        width = self.width
        height = self.height
        self.fill_matrix = np.zeros((width - 1, height - 1), dtype=bool)
        mutation = other.number * norm
        # mutujemy liczbe kolek
        # ograniczenia na maksa i minimum
        self.number = round(other.number + mutation)
        if self.number > (width - 1) * (height - 1):
            self.number = (width - 1) * (height - 1)
        elif self.number < 1:
            self.number = 1

        # Przepisanie kolek z other do self
        for i in range(min(self.number, other.number)):
            self.circles.append(other.circles[i])
            self.fill_matrix[other.circles[i][0] - 1, other.circles[i][1] - 1] = True
        # W przypadku gdy trzeba dodac wiecej kolek
        for i in range(self.number - other.number):
            # To moj geniusz zeby nie losowac bez sensu
            # Empty fields - [0] - x values, [1] - y values
            empty_fields = np.where(self.fill_matrix == False)
            nr = randint(0, empty_fields[0].__len__())
            x = empty_fields[0][nr] + 1
            y = empty_fields[1][nr] + 1
            self.fill_matrix[x - 1, y - 1] = True
            self.circles.append((x, y, self.radius))

        # Mutacja co 4 kolka
        # todo przemyslec zeby ta mutacja nie byla taka losowa
        for i in range(1, self.number, 4):
            empty_fields = np.where(self.fill_matrix == False)
            if empty_fields[0].__len__() == 0:
                break
            nr = randint(0, empty_fields[0].__len__())
            x = empty_fields[0][nr] + 1
            y = empty_fields[1][nr] + 1
            x_old = self.circles[i][0]
            y_old = self.circles[i][1]
            self.fill_matrix[x_old - 1, y_old - 1] = False
            del(self.circles[i])
            self.fill_matrix[x - 1, y - 1] = True
            self.circles.append((x, y, self.radius))
