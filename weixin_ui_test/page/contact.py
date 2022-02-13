from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from weixin_ui_test.page.base import Base


class Contact(Base):

    def add_member_btn(self):
        self.steps("../page/steps.yaml")

    def add_member(self,info):
        self._params = info
        self.steps("../page/steps.yaml")

    def find_member(self,member):
        self.wait_and_clickable((By.CSS_SELECTOR,".member_colRight_memberTable_th_Checkbox"))
        elements = self.finds(By.CSS_SELECTOR,'.member_colRight_memberTable_tr>td:nth-child(2)')
        element: WebElement

        flag = False

        for element in elements:
            if element.get_attribute('title') == member:
                flag = True

        return flag


if __name__ == '__main__':
    url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    options = Options()
    options.debugger_address = "127.0.0.1:9222"

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    driver.implicitly_wait(10)

    elements = driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_tr>td:nth-child(2)')
    element: WebElement
    member = "小米"
    for element in elements:
        if element.get_attribute('title') == member:
            print("get")

    print("opppsss")