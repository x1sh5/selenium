from selenium import webdriver

driver = webdriver.Firefox()
driver.get()
link = "www.baidu.com"

js='window.open(link);'
driver.execute_script(js)
