import os,sys

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)
sys.path.append("D:\\PycharmProjects\\pythonProject1\\venv\Lib\\site-packages")

import inspect
import json
import os

import requests
import yaml

class BaseApi:

    _params =  {}
    def request(self,data):
        res = requests.request(**data)
        return res

    def get_token(self):
        corpid = "wwc9118deabe4d6e6c"
        corpsecret = "PrOMHKQWOy5MvyhoXdqiwoGpG3ux0nRuW_D_z0LKxRY"

        data = {
            "method" : "get",
            "url" : "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params" :{
                "corpid" : corpid,
                "corpsecret" : corpsecret
            }
        }

        res = self.request(data)
        return res.json()['access_token']

    def steps(self,path):
        with open(path, encoding="utf-8") as f:
            steps = yaml.safe_load(f)

        raw = json.dumps(steps)
        for key , value in self._params.items():
            raw = raw.replace(f'${{{key}}}',value)
        steps = json.loads(raw)

        name = inspect.stack()[1].function

        steps[name]['url'] =self.get_env()+steps[name]['url']

        return steps[name]


    def get_env(self):
        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'api/params.yaml'), encoding="utf-8") as f:
            data = yaml.safe_load(f)

        key = data['env']["default"]
        env = data['env']["config"][key]

        return env




if __name__ == '__main__':
    b = BaseApi()
    # print(b.get_token())
    # b.steps("../api/params.yaml")
    print(b.get_env("../api/params.yaml"))