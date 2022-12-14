import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

url = "https://www.baidu.com"
driver.get(url)


# 1-id定位
# driver.find_element(By.ID, "kw").send_keys("python")
# time.sleep(2)
# driver.find_element(By.ID, "su").click()
# time.sleep(2)

# 2-name定位
# driver.find_element(By.NAME, "wd").send_keys("python")
# time.sleep(2)
# driver.find_element(By.ID, "su").click()
# time.sleep(2)

# 3-tag name定位
# input比较多不适合用tag_name定位
# driver.find_element(By.TAG_NAME, "input").send_keys("python")
# time.sleep(2)
# driver.find_element(By.ID, "su").click()
# time.sleep(2)

# 4-clas name定位
# driver.find_element(By.CLASS_NAME, "s_ipt").send_keys("python")
# time.sleep(2)
# driver.find_element(By.ID, "su").click()
# time.sleep(2)

# 5-css selector定位
# driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("python")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "#su").click()
# time.sleep(2)

# driver.find_element(By.CSS_SELECTOR, "input[name='wd']").send_keys("python")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
# time.sleep(2)

# driver.find_element(By.CSS_SELECTOR, ".s_ipt").send_keys("python")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "input[class='bg s_btn']").click()
# time.sleep(2)

# 6-xpath 定位
driver.find_element(By.XPATH, "//form[@name='f']/span/input[@id='kw']").send_keys("python")
time.sleep(2)

driver.find_element(By.XPATH, "//form[@name='f']/span/input[@value='百度一下']").click()
time.sleep(2)

print(driver.current_url)




