import json_
import field

if __name__ == "__main__":

    start, finish, polygons = json_.read_json("../data/test_1.json")
    tmp_field = field.Field(start, finish, polygons)
    print(tmp_field.find_neighbours(field.Point(1, 1)))