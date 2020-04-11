import numpy as np
from numpy.random import randint
import IntersectArea

from Element import Element


class Member:
    radius = None
    width = None
    height = None
    forbidden_places = None
    forbidden_nr = 0
    rest_areas = None

    @staticmethod
    def set_restricted_areas(rest_areas):
        Member.forbidden_places = np.full((Member.width - 1, Member.height - 1), Element.Empty, dtype=Element)
        for (x_min, x_max, y_min, y_max) in rest_areas:
            forbidden_width = x_max - x_min - 1
            forbidden_height = y_max - y_min - 1
            if forbidden_height > 0 and forbidden_width > 0:
                Member.forbidden_places[x_min: x_min + forbidden_width, y_min: y_min + forbidden_height] \
                    = Element.Forbidden
        Member.forbidden_nr = np.count_nonzero(Member.forbidden_places == Element.Forbidden)

    def __init__(self, add_circles=True):
        self.circles = []
        self.fill_matrix = self.forbidden_places.copy()
        if add_circles:
            pts_nr = (self.width - 1) * (self.height - 1) - self.forbidden_nr
            # randint(a, b) - random between <a, b)
            self.number = randint(pts_nr / 2, pts_nr + 1)

            for i in range(self.number):
                empty_fields = np.where(self.fill_matrix == Element.Empty)
                free_field = randint(0, empty_fields[0].__len__())
                # (x, y) - coordinates on the field, matrix contains (x-1)*(y-1) elements
                x = empty_fields[0][free_field] + 1
                y = empty_fields[1][free_field] + 1
                self.fill_matrix[x - 1, y - 1] = Element.Taken
                self.circles.append((x, y, self.radius))

    def print_circles(self):
        output = open("output.txt", "w")
        for c in self.circles:
            output.write("circle" + str(c) + ";\n")
        output.close()

    def mutate(self, other, mutation):
        # mutation = other.number * norm  # mutation can be positive and negative
        print("norm", mutation)
        # Mutate number of circles
        self.number = int(other.number + mutation)  # change number of sprinklers
        if self.number > (self.width - 1) * (self.height - 1) - self.forbidden_nr:
            self.number = int((self.width - 1) * (self.height - 1) - self.forbidden_nr)
        elif self.number < 1:
            self.number = 1

        # Copy circles from parent to child (child may have more circles than parent)
        indexes_of_circles_to_copy = np.random.choice(other.number, min(self.number, other.number), replace=False)
        for i in indexes_of_circles_to_copy:
            self.circles.append(other.circles[i])
            self.fill_matrix[other.circles[i][0] - 1, other.circles[i][1] - 1] = Element.Taken

        # If child have more circles than parent - add the rest
        empty_fields = np.where(self.fill_matrix == Element.Empty)
        indexes_of_circles = np.arange(self.number - other.number)
        np.random.shuffle(indexes_of_circles)
        for i in indexes_of_circles:
            x = empty_fields[0][i] + 1
            y = empty_fields[1][i] + 1
            self.fill_matrix[x - 1, y - 1] = Element.Taken
            self.circles.append((x, y, self.radius))

        # Mutate every 5th circle
        if self.number != (self.width-1)*(self.height-1) - self.forbidden_nr:
            for i in range(0, self.number, 5):
                mutual_area = self.calculate_mutual_area(True)
                circle_key_old = max(mutual_area, key=lambda k: mutual_area[k])
                x_old = circle_key_old[0]
                y_old = circle_key_old[1]

                self.circles.remove((x_old, y_old, self.radius))
                self.fill_matrix[x_old - 1, y_old - 1] = Element.Empty

                mutual_area = self.calculate_mutual_area(False)
                circle_key_new = max(mutual_area, key=lambda k: mutual_area[k])
                x_new = circle_key_new[0]
                y_new = circle_key_new[1]

                self.circles.append((x_new, y_new, self.radius))
                self.fill_matrix[x_new - 1, y_new - 1] = Element.Taken

    def calculate_mutual_area(self, busy):
        mutual_area = {}
        area = 0
        empty_fields = np.where(self.fill_matrix == Element.Empty)
        taken_fields = np.where(self.fill_matrix == Element.Taken)
        if busy:
            for i in range(taken_fields[0].__len__()):  # which count
                x_i = taken_fields[0][i] + 1
                y_i = taken_fields[1][i] + 1
                for j in range(taken_fields[0].__len__()):  # comparison
                    x_j = taken_fields[0][j] + 1
                    y_j = taken_fields[1][j] + 1
                    if x_j == x_i and y_i == y_j:
                        continue
                    area = area + IntersectArea.intersect_area((x_i, y_i, self.radius), (x_j, y_j, self.radius))
                mutual_area.update({(x_i, y_i, self.radius): area})
                area = 0
        else:
            for i in range(empty_fields[0].__len__()):  # which count
                x_i = empty_fields[0][i] + 1
                y_i = empty_fields[1][i] + 1
                for j in range(taken_fields[0].__len__()):  # comparison
                    x_j = taken_fields[0][j] + 1
                    y_j = taken_fields[1][j] + 1
                    area = area + IntersectArea.intersect_area((x_i, y_i, self.radius), (x_j, y_j, self.radius))
                cover_area = (np.pi * self.radius * self.radius) - IntersectArea.void_area((x_i, y_i, self.radius),
                                                                                           self.width,
                                                                                           self.height, self.rest_areas) - area
                mutual_area.update({(x_i, y_i, self.radius): cover_area})
                area = 0
        return mutual_area
