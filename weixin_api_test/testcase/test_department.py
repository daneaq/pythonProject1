import pytest

from weixin_api_test.api.department import Department


class TestDepaerment:

    @pytest.mark.parametrize("name,name_en,parentid,order,id", [('gz', 'RDGZ', '1', '1', '2'),
                                                                ('nj', 'RDNJ', '1', '2', '3')])
    def test_creat_department(self,name,name_en,parentid,order,id):
        self.department = Department()

        result = self.department.create_department(name,name_en,parentid,order,id)
        print(result.json())

        assert result.json()['errcode'] == "0"

    @pytest.mark.parametrize("id", "5")
    def test_delete_department(self,id):
        self.department = Department()

        result = self.department.delete_department(id)
        print(result.json())

        assert result.json()['errcode'] == "0"