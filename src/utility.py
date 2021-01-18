import field
import geometry


def process_polygon(polygon: dict):
    """
    Обрабатывает данные препятствия.
    Возвращает его данные в виде объектов класса Point.
    """
    inner_point = field.Point(polygon["x"], polygon["y"])
    points = list()

    for coords in polygon["vertices"]:
        points.append(field.Point(coords["x"], coords["y"]))

    return {"inner": inner_point, "coords": points}


def check_is_inside_polygon(point, polygon: dict):

    lines = list()
    points = polygon["coords"]

    # Обработка списка точек, формирование прямых
    points.append(points[0])
    for idx in range(len(points) - 1):
        lines.append(geometry.Line(points[idx], points[idx + 1]).calculate(point))

    if len(list(filter(lambda x: x <= 0, lines))) == len(lines):
        return True
    return False


if __name__ == "__main__":
    test_polygon = {
        "coords": [field.Point(1, 1), field.Point(3, 6), field.Point(7, -1)]
    }
    print(check_is_inside_polygon(field.Point(1, 4), test_polygon))
