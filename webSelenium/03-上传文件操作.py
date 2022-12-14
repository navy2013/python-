from selenium import webdriver
import os, time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('upload_file.html')
driver.get(file_path)

driver.find_element(By.NAME,'file').send_keys('D:\银河\图片\双旦.jpg')
time.sleep(3)

driver.quit()
