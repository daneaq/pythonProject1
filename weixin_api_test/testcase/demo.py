import os

import requests
import yaml


def get_env(path):
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # print(data)

    key = data['env']["defualt"]
    env = data['env']["config"][key]

    print(env)


# get_env("../testcase/demo.yaml")

# proxy ={
#     'http':"192.168.3.25:8888"
# }
# corpid = "wwc9118deabe4d6e6c"
# corpsecret = "PrOMHKQWOy5MvyhoXdqiwoGpG3ux0nRuW_D_z0LKxRY"
#
# data = {
#     "method" : "get",
#     "url" : "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
#     "params" :{
#         "corpid" : corpid,
#         "corpsecret" : corpsecret
#     }
# }
# res = requests.get(url=data['url'],params=data['params'],proxies=proxy)
# print(res.text)

file = os.path.join(os.path.dirname(os.path.dirname(__file__)),'api/params.yaml')

print(file)