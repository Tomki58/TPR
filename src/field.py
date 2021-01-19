from itertools import chain

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


class Field:
    def __init__(self, start_point: Point, finish_point: Point, polygons: list):
        # self.start_point = start_point
        self.points = list()
        for y in reversed(range(51)):
            row = list()
            # Заполнение строки
            for x in range(51):
                print(x, y)
                tmp_point = Point(x, y)
                if any(
                    [
                        check_is_inside_polygon(tmp_point, polygon)
                        for polygon in polygons
                    ]
                ):
                    tmp_point.d = 1e2

                row.append(tmp_point)

            self.points.append(row)

        # self.points = [[-1 for i in range(51)] for j in range(51)]

    def find_neighbours(self, point: Point):
        """Находит доступных соседей точки."""
        neighbours = list()
        for x in range(point.x - 1, point.x + 2):
            for y in range(point.y - 1, point.y + 2):
                try:
                    potential_neighbour = self.get_point(x, y)
                except:
                    continue
                else:
                    neighbours.append(potential_neighbour)

        return neighbours

    def send_wave(self):
        """Посылает волну."""
        self.start_point = self.get_point(2, 2)
        self.finish_point = self.get_point(48, 48)
        points_queue = iter([self.get_point(2, 2)])

        curr_point = next(points_queue)
        curr_point.d = 0

        while self.finish_point.d == -1:
            neighbours = self.find_neighbours(curr_point)
            neighbours = [
                neigh
                for neigh in self.find_neighbours(curr_point)
                if (neigh != self.start_point and neigh.d == -1)
            ]
            for neighbour in neighbours:
                neighbour.d = curr_point.d + 1
            points_queue = chain(points_queue, iter(neighbours))
            curr_point = next(points_queue)

    def recover_path(self):
        """Восстанавливает найденный путь."""
        curr_point = self.finish_point
        path = [curr_point]
        while curr_point != self.start_point:
            suitable_neighbour = [
                neighbour
                for neighbour in self.find_neighbours(curr_point)
                if curr_point.d - neighbour.d == 1
            ][0]
            path.append(suitable_neighbour)
            curr_point = suitable_neighbour

        path_dict = [{"cx": path_point.x, "cy": path_point.y} for path_point in path]
        return path_dict

    def get_point(self, x, y) -> Point:
        if x < 0 or y < 0:
            raise IndexError()
        else:
            return self.points[50 - y][x]

    def print_field(self):
        for row in self.points:
            print(row)
