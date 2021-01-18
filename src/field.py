from utility import check_is_inside_polygon


class Point:
    def __init__(self, x=None, y=None, d: int = -1):
        self.x = x
        self.y = y
        self.d = d

    def __eq__(self, point):
        return True if (self.x == point.x and self.y == point.y) else False

    def __repr__(self):
        return "%d:%d" % (self.x, self.y)
        # return "%d" % self.d


# TODO: распространение волны


class Field:
    def __init__(self, start_point: Point, finish_point: Point, polygons: list):
        self.start_point = start_point
        self.points = list()
        for y in reversed(range(51)):
            row = list()
            # Заполнение строки
            for x in range(51):
                tmp_point = Point(x, y)
                if any(
                    [
                        check_is_inside_polygon(tmp_point, polygon)
                        for polygon in polygons
                    ]
                ):
                    tmp_point.d = 1e3

                row.append(tmp_point)

            self.points.append(row)

    def find_neighbours(self, point: Point):
        neighbours = list()
        for x in range(point.x - 1, point.x + 2):
            for y in range(point.y - 1, point.y + 2):
                try:
                    potential_neighbour = self.get_point(x, y)
                except:
                    continue
                else:
                    if (
                        potential_neighbour.d == -1
                        and potential_neighbour != self.start_point
                        and potential_neighbour != point
                    ):
                        neighbours.append(potential_neighbour)

        return neighbours

    def get_point(self, x, y) -> Point:
        if x < 0 or y < 0:
            raise IndexError()
        else:
            return self.points[50 - y][x]

    def wave(self):
        points_queue = [self.get_point(2, 2)]
        finish_point = self.get_point(50, 50)
        while finish_point.d == -1:
            for curr_point in points_queue:
                neighbours = self.find_neighbours(curr_point)
                for neighbour in neighbours:
                    neighbour.d += 1

    def __repr__(self):
        for row in self.points:
            print(row)
