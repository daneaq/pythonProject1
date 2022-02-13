import inspect

import yaml


from weixin_ui_test.page.app import App


class TestBase:

    # def setup(self):
    #     self.main = App().start().main()

    def __init__(self):
        self.main = App().start().main()

    def test_datas(self,path):

        with open(path,encoding="utf-8") as f:
            datas = yaml.safe_load(f)

        instance1 = inspect.stack()[1].function
        instance = inspect.stack()[1].function

        data_list = []
        data:dict
        for data in datas[instance]:
            values = tuple(data.values())
            data_list.append(values)

        return data_list



