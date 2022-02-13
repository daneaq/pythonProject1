import pytest

from weixin_api_test.api.department import Department


class TestDepaerment:

    @pytest.mark.parametrize("name,name_en,parentid,order,id", [('aa', '', '1', '', '')])
    def test_creat_department(self,name,name_en,parentid,order,id):
        self.department = Department()

        result = self.department.create_department(name,name_en,parentid,order,id)
        print(result.json())

        assert result.json()['errcode'] == "0"