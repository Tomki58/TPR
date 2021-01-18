import field
import utility


class Line:
    def __init__(self, point_1, point_2):
        self.coeff_x = point_1.y - point_2.y
        self.coeff_y = point_2.x - point_1.x
        self.coeff_c = point_1.x * point_2.y - point_2.x * point_1.y

    def calculate(self, point):
        return self.coeff_x * point.x + self.coeff_y * point.y + self.coeff_c

    def __repr__(self):
        return "%dx + (%d)y + (%d) = 0" % (self.coeff_x, self.coeff_y, self.coeff_c)


if __name__ == "__main__":
    l_1 = Line(field.Point(1, 1), field.Point(3, 6))
    l_2 = Line(field.Point(3, 6), field.Point(7, -1))
    l_3 = Line(field.Point(7, -1), field.Point(1, 1))

    # print(l_1)
    # print(l_2)
    # print(l_3)
