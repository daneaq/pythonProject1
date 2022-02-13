import inspect
import json

import yaml


def replace():

    params = {
        "name":"1233"
    }

    with open("../page/steps.yaml") as f:
        datas = yaml.safe_load(f)

    print(json.dumps(datas['add_yaml']))
    str = json.dumps(datas['add_yaml'])

    for key,value in params.items():
        print(key,value)
        str = str.replace(f'${{{key}}}',value)

    print(str)


def steps(file, params):
    with open(file) as f:
        steps = yaml.safe_load(f)

    raw = json.dumps(steps)
    for key,value in params.items():
        raw = raw.replace(f'{{{key}}}',value)

    datas = json.loads(raw)
    name = inspect.stack()[1].function

    for step in datas[name]:
        if 'action' in step:
            print(step['by'], step['locator'])
            # if 'click' == step['action']:
                # element.click()
                # print(step['by'],step['locator'])
            if 'input' == step['action']:
                print(step['value'])


def demo():
    params = {
        'name':'1213'
    }
    steps("../page/steps.yaml",params)

demo()


def yaml_create():
    datas = {


    }


