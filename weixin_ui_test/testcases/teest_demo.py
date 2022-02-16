import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


#指定运行主机与端口号

driver = webdriver.Remote(
     command_executor='http://localhost:4444/wd/hub',
     desired_capabilities=DesiredCapabilities.CHROME)

driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("hello")
driver.find_element_by_id("su").click()
time.sleep(2)
driver.close()