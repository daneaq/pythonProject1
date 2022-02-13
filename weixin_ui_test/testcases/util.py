import inspect

import yaml

def get_test_data(path):
    with open(path, encoding="utf-8") as f:
        datas = yaml.safe_load(f)

    instance11 = inspect.stack()[1]
    instance = inspect.stack()[1].function

    data_list = []
    data: dict
    for data in datas[instance]:
        values = tuple(data.values())
        data_list.append(values)

    return data_list