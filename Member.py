import numpy as np
from numpy.random import randint

from Element import Element


class Member:
    radius = None
    width = None
    height = None
    forbidden_places = None
    forbidden_nr = 0

    @staticmethod
    def set_restricted_areas(rest_areas):
        Member.forbidden_places = np.full((Member.width - 1, Member.height - 1), Element.Empty, dtype=Element)
        for (x_min, x_max, y_min, y_max) in rest_areas:
            forbidden_width = x_max - x_min - 1
            forbidden_height = y_max - y_min - 1
            if forbidden_height > 0 and forbidden_width > 0:
                Member.forbidden_places[x_min: x_min + forbidden_width, y_min: y_min + forbidden_height] = Element.Forbidden
        Member.forbidden_nr = np.count_nonzero(Member.forbidden_places == Element.Forbidden)

    def __init__(self, add_circles=True):
        if add_circles:
            width = self.width
            height = self.height
            radius = self.radius
            self.circles = []
            self.fill_matrix = self.forbidden_places.copy()
            pts_nr = (width - 1) * (height - 1) - self.forbidden_nr
            # randint(a, b) - random between <a, b)
            self.number = randint(pts_nr / 2, pts_nr + 1)

            for i in range(self.number):
                empty_fields = np.where(self.fill_matrix == Element.Empty)
                free_field = randint(0, empty_fields[0].__len__())
                # (x, y) - coordinates on the field, matrix contains (x-1)*(y-1) elements
                x = empty_fields[0][free_field] + 1
                y = empty_fields[1][free_field] + 1
                self.fill_matrix[x - 1, y - 1] = Element.Taken
                self.circles.append((x, y, radius))

    def print_circles(self):
        output = open("output.txt", "w")
        for c in self.circles:
            output.write("circle" + str(c) + ";\n")
        output.close()

    def mutate(self, other, norm):
        self.circles = []
        width = self.width
        height = self.height
        radius = self.radius
        self.fill_matrix = self.forbidden_places.copy()
        mutation = other.number * norm  # mutation can be positive and negative
        # Mutate number of circles
        self.number = round(other.number + mutation) # change number of sprinklers
        if self.number > (width - 1) * (height - 1) - self.forbidden_nr:
            self.number = (width - 1) * (height - 1) - self.forbidden_nr
        elif self.number < 1:
            self.number = 1

        # Copy circles from parent to child (child may have more circles than parent)
        indexes_of_circles_to_copy = np.random.choice(other.number, min(self.number, other.number), replace=False)
        for i in indexes_of_circles_to_copy:
            self.circles.append(other.circles[i])
            self.fill_matrix[other.circles[i][0] - 1, other.circles[i][1] - 1] = Element.Taken

        # If child have more circles than parent - add the rest
        for i in range(self.number - other.number):
            # Empty fields - [0] - x values, [1] - y values
            empty_fields = np.where(self.fill_matrix == Element.Empty)
            free_field = randint(0, empty_fields[0].__len__())
            x = empty_fields[0][free_field] + 1
            y = empty_fields[1][free_field] + 1
            self.fill_matrix[x - 1, y - 1] = Element.Taken
            self.circles.append((x, y, radius))

        # Mutate every 5th circle
        for i in range(0, self.number, 5):
            circle_to_mutate = randint(0, self.number)
            empty_fields = np.where(self.fill_matrix == Element.Empty)
            if empty_fields[0].__len__() == 0:
                break
            x_old = self.circles[circle_to_mutate][0]
            y_old = self.circles[circle_to_mutate][1]
            x_or_y = randint(0, 2)  # Mutate only x or only y, not both
            if x_or_y:
                x_new = round(x_old + x_old * norm)
                y_new = y_old
                if x_new >= width - 1:
                    x_new = width - 1
                elif x_new < 1:
                    x_new = 1
            else:
                x_new = x_old
                y_new = round(y_old + y_old * norm)
                if y_new >= height - 1:
                    y_new = height - 1
                elif y_new < 1:
                    y_new = 1
            distance = []  # Distance from empty places - mean square
            for k in range(empty_fields[0].__len__()):
                dis = (empty_fields[0][k] - x_new) ** 2 + (empty_fields[1][k] - y_new) ** 2
                distance.append(dis)
                if dis < 1:
                    break

            x_new = empty_fields[0][np.argmin(distance)] + 1
            y_new = empty_fields[1][np.argmin(distance)] + 1
            # Remove circle before mutation
            self.fill_matrix[x_old - 1, y_old - 1] = Element.Empty
            self.circles.remove((x_old, y_old, self.radius))
            # Add circle after mutation
            self.fill_matrix[x_new - 1, y_new - 1] = Element.Taken
            self.circles.append((x_new, y_new, self.radius))
