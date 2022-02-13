import inspect
import time

import pytest
import yaml

from weixin_ui_test.page.app import App
from weixin_ui_test.page.main import Main
from weixin_ui_test.testcases.test_base import TestBase
from weixin_ui_test.testcases.util import get_test_data


class TestContact(TestBase):

    def get_data(self):
        return self.test_datas("../testcases/testcases.yaml")

    @pytest.mark.parametrize("name,acctid,mail,phone",get_data())
    def test_add_contact(self,name,acctid,mail,phone):

        contact = self.main.goto_contact()
        time.sleep(10)
        contact.add_member_btn()
        time.sleep(10)

        info = {
            "name" : name,
            "acctid" : acctid,
            "mail" : mail,
            "phone":phone
        }
        contact.add_member(info)

        assert contact.find_member(info['name'])

