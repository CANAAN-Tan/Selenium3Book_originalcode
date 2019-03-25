"""
*  switch_to.frame()  进入表单
*  switch_to.default_content()  退出表单至根页面
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.126.com")
sleep(2)

login_frame = driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
driver.switch_to.frame(login_frame)
driver.find_element_by_name("email").send_keys("username")
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()

driver.quit()
