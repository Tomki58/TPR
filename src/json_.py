import json

import field
import utility


def read_json(filepath: str) -> tuple:
    """
    Считывает json файл и генерирует три значения:\n
    Индексы выхода:\n
    0 - стартовая точка,\n
    1 - конечная точка,\n
    2 - массив препятствий
    """

    with open(filepath, "r") as read_file:
        json_deserialized = json.load(read_file)

    start_point = field.Point(**(json_deserialized["start"]))
    finish_point = field.Point(**(json_deserialized["finish"]))

    polygons = list()
    for polygon in json_deserialized["polygons"]:
        polygons.append(utility.process_polygon(polygon))

    return (start_point, finish_point, polygons)


def save_as_json(content, filepath: str = "./data/result.json"):
    """Сохраняет содержимое в виде объекта json."""
    json_serialized = json.dumps(content)
    with open(filepath, "w") as write_file:
        write_file.write(json_serialized)


if __name__ == "__main__":
    start, _, polygons = read_json("../data/test_1.json")
