import inspect
import json
import time

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from weixin_ui_test.page.wrapper import handle_black


class Base:
    _driver:webdriver = None
    _params = {}

    def __init__(self,driver:webdriver):
        self._driver = driver

    def find(self,locator,value=None):
        element : WebElement

        if isinstance(locator,tuple):
           element = WebDriverWait(self._driver,30).until(EC.presence_of_element_located(locator))
        else:
            element = WebDriverWait(self._driver,30).until(EC.presence_of_element_located((locator,value)))

        return element

    def finds(self, locator, value=None):
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator,value)
        return elements

    def wait_and_clickable(self,locator):
        WebDriverWait(self._driver,60).until(EC.element_to_be_clickable(locator))


    def input(self,text,locator,value=None):

        element = self.find(locator,value)
        element.clear()
        element.send_keys(text)

    def steps(self,path):
        with open(path,encoding='utf-8') as f:
            steps =yaml.safe_load(f)

        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace(f'${{{key}}}',value)

        steps = json.loads(raw)
        name = inspect.stack()[1].function

        for step in steps[name]:
            if 'action' in step:
                if 'by' in step:
                    element = self.find(step['by'], step['locator'])
                    if 'click' == step['action']:
                        element.click()
                    if 'send_keys' == step['action']:
                        element.send_keys(step['value'])

if __name__ == "__main__":

    options = Options()
    options.debugger_address = "127.0.0.1:9222"

    driver = webdriver.Chrome(options=options)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    bs = Base(driver)
    #
    # # ele = bs.find("id","menu_contacts")
    # # ele.click()
    # # time.sleep(5)
    # ele = bs.find("css selector",".js_has_member>div:nth-child(1)>a:nth-child(2)")
    # ele.click()
    print(1111111)
    def add_yaml():
        bs.steps("../page/steps.yaml")
    add_yaml()

