from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from lxml import etree

driver = webdriver.Firefox()
driver.get('https://github.com/search?o=desc&q=scrapy&s=updated&type=Repositories&utf8=%E2%9C%93')
current_wind = driver.current_window_handle
print(current_wind)
#driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div/div/div/form/label/input[1]").clear()
#driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div/div/div/form/label/input[1]").send_keys("scrapy")
#driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div/div/div/form/label/input[1]").send_keys(Keys.ENTER)
sleep(5)
urls = driver.find_elements_by_xpath("/html/body/div[4]/div[1]/div[2]/div/div[1]/ul//div/div[1]/h3/a")
for url in urls:
    link = url.text
    print(link)
    target = driver.find_element_by_link_text(link)
    actions = ActionChains(driver)
    actions.move_to_element(target)
    actions.click(target)
    actions.perform()
    sleep(2)
    print(driver.current_window_handle)
    driver.switch_to_window(driver.window_handles[0]) #此行代码用来定位当前页面
    #for handle in driver.window_handles:
        #方法二，始终获得当前最后的窗口，所以多要多次使用
        #driver.switch_to_window(handle)
    download_btn = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div[1]/div[5]/details/summary")
    #if download_btn.is_displayed():
    ActionChains(driver).move_to_element(download_btn).click(download_btn).perform()
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div[1]/div[5]/details/div/div/div[2]/a[2]").click()
    #driver.back()
    
    #js='window.open("www.baidu.com");'
    #driver.execute_script(js)
    #driver.get(link)
    #driver.find_element_by_class_name("btn btn-sm btn-primary").click()
    #ActionChains(driver).sendkeys(Keys.ENTER)
    #sleep(2)
    #driver.close

#js='window.open("https://www.sogou.com");'
#driver.execute_script(js)
#print(current_window)
#handles = driver.window_handles
#print(handles)
#driver.switch_to_window(current_window)
#sleep(3)
