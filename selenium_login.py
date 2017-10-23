from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver = webdriver.Firefox()
driver.get("https://www.zhihu.com/#signin")
#action = ActionChains(driver)
login_btn = driver.find_element_by_link_text(u"登录")

ActionChains(driver).move_to_element(login_btn).click(login_btn).perform()

switch_btn = driver.find_element_by_class_name("signin-switch-password")

ActionChains(driver).move_to_element(switch_btn).click(switch_btn).perform()
driver.find_element_by_name("account").clear()
driver.find_element_by_name("account").send_keys("13364034436")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("Xxp420523")
driver.find_element_by_css_selector("button.sign-button.submit").click()
sleep(10)
