from selenium import webdriver
import os, time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# driver= webdriver.Chrome()
# file_path = 'file:///' + os.path.abspath('drop_down.html')
# driver.get(file_path)
# time.sleep(2)
#
# ele=driver.find_element(By.ID,'ShippingMethod')
# ele.find_element(By.XPATH,'//option[@value="10.69"]').click()
# time.sleep(3)
#
# driver.quit()


# 百度设置

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.baidu.com")
# 定位设置
ele = driver.find_element(By.ID, 's-usersetting-top')
time.sleep(2)
# 悬停
ActionChains(driver).move_to_element(ele).perform()
time.sleep(2)
# 定位搜索设置
driver.find_element(By.LINK_TEXT, '搜索设置').click()
time.sleep(2)
# 每页20条
driver.find_element(By.XPATH, '//form[@name="f2"]/div/ul/li[3]/span[2]/span[2]').click()
time.sleep(2)
# 保存设置
driver.find_element(By.LINK_TEXT, '保存设置').click()
time.sleep(2)

# 弹窗确认
# driver.switch_to.alert.accept()
driver.switch_to.alert.accept()
time.sleep(2)

# 跳转百度首页搜索，返回20条数据
driver.find_element(By.ID, "kw").send_keys("selenium")
driver.find_element(By.ID, "su").click()
time.sleep(5)

driver.quit()
