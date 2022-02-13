from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from weixin_ui_test.page.main import Main


class App:

    _driver :webdriver = None

    def start(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"

        self._driver = webdriver.Chrome(options=options)
        self._driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        self._driver.implicitly_wait(10)

        return self

    def main(self):
        return Main(self._driver)