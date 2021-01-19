import json_
import field

import pickle

if __name__ == "__main__":
    try:
        with open("./data/field.pickle", "rb") as f:
            tmp_field = pickle.load(f)
    except:
        start, finish, polygons = json_.read_json("data/test_1.json")
        tmp_field = field.Field(start, finish, polygons)
        with open("./data/field.pickle", "wb") as f:
            pickle.dump(tmp_field, f)

    # tmp_field.print_field()
    tmp_field.send_wave()
    path = tmp_field.recover_path()
    print(path)
    json_.save_as_json(path)
