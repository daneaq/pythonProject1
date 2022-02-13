import pytest

from weixin_api_test.api.base import BaseApi
import os
import sys

file = os.path.join(os.path.dirname(os.path.dirname(__file__)),'api/params.yaml')


class Department(BaseApi):


    def create_department(self,name,name_en,parentid,order,id):
        self._params = {
            "access_token": self.get_token(),
            "name": name,
            "name_en": name_en,
            "parentid": parentid,
            "order": order,
            "id": id
        }
        data = self.steps(os.path.join(os.path.dirname(os.path.dirname(__file__)),'api/params.yaml'))

        res  = self.request(data)

        return res

    def delete_department(self,id):
        self._params = {
            "access_token" : self.get_token(),
            "id":id
        }
        data = self.steps(os.path.join(os.path.dirname(os.path.dirname(__file__)),'api/params.yaml'))

        res = self.request(data)

        return res

