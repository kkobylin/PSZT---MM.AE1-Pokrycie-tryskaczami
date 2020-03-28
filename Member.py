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
            self.number = randint(1, pts_nr + 1)

            for i in range(self.number):
                empty_fields = np.where(self.fill_matrix == False)
                nr = randint(0, empty_fields[0].__len__())
                x = empty_fields[0][nr] + 1
                y = empty_fields[1][nr] + 1
                # Matrix enumerate from 0, (x, y) - coordinates on the field
                self.fill_matrix[x - 1, y - 1] = True
                self.circles.append((x, y, radius))

    def print_circles(self):
        output = open("output.txt", "w")  # otwieranie pliku
        for c in self.circles:
            output.write("circle" + str(c) + ";\n")
        output.write("grid on")
        output.close()

    def mutate(self, other, norm):
        self.circles = []
        width = self.width
        height = self.height
        self.fill_matrix = np.zeros((width - 1, height - 1), dtype=bool)
        mutation = other.number * norm
        # Mutate number of circles
        self.number = round(other.number + mutation)
        if self.number > (width - 1) * (height - 1):
            self.number = (width - 1) * (height - 1)
        elif self.number < 1:
            self.number = 1

        # Copy circles from parent to child (child may have more circles than parent)
        ind_of_circ_to_copy = np.random.choice(other.number, min(self.number, other.number), replace=False)
        for i in ind_of_circ_to_copy:
            self.circles.append(other.circles[i])
            self.fill_matrix[other.circles[i][0] - 1, other.circles[i][1] - 1] = True

        # If child have more circles than parent - add the rest
        for i in range(self.number - other.number):
            # Empty fields - [0] - x values, [1] - y values
            empty_fields = np.where(self.fill_matrix == False)
            nr = randint(0, empty_fields[0].__len__())
            x = empty_fields[0][nr] + 1
            y = empty_fields[1][nr] + 1
            self.fill_matrix[x - 1, y - 1] = True
            self.circles.append((x, y, self.radius))

        # Mutate every 3rd circle
        #todo moze da sie to jakos zoptymalizowac
        for i in range(0, self.number, 3):

            # index of circle to mutate
            nr = randint(0, self.number)
            empty_fields = np.where(self.fill_matrix == False)
            if empty_fields[0].__len__() == 0:
                break
            x_old = self.circles[nr][0]
            y_old = self.circles[nr][1]
            x_new = round(x_old + x_old * norm)
            y_new = round(y_old + y_old * norm)
            if x_new >= width - 1:
                x_new = width - 1
            elif x_new < 1:
                x_new = 1
            if y_new >= height - 1:
                y_new = height - 1
            elif y_new < 1:
                y_new = 1

            # Distance from empty places - mean square
            distance = []
            for k in range(empty_fields[0].__len__()):
                dis = (empty_fields[0][k] - x_new) ** 2 + (empty_fields[1][k] - y_new) ** 2
                distance.append(dis)

            x_new = empty_fields[0][np.argmin(distance)] + 1
            y_new = empty_fields[1][np.argmin(distance)] + 1
            # Remove circle before mutation
            self.fill_matrix[x_old - 1, y_old - 1] = False
            del(self.circles[nr])
            # Add circle after mutation
            self.fill_matrix[x_new - 1, y_new - 1] = True
            self.circles.append((x_new, y_new, self.radius))
