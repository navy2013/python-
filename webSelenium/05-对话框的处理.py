from selenium import webdriver
from time import sleep
import os
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By

if 'HTTP_PROXY' in os.environ: del os.environ['HTTP_PROXY']
dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('modal.html')
dr.maximize_window()
dr.get(file_path)

# 打开对话框
dr.find_element(By.ID, 'show_modal').click()
sleep(5)
# 点击对话框中的链接
# 由于对话框中的元素被蒙板所遮挡，直接点击会报 Element is not clickable 的错误
# 所以使用 js 来模拟 click
link = dr.find_element(By.ID, 'myModal').find_element(By.ID, 'click')
dr.execute_script('arguments[0].click()', link)
sleep(4)


# 关闭对话框
# dr.find_element(By.CLASS_NAME, 'modal-footer').find_elements(By.TAG_NAME, 'button')[0].click()
dr.quit()
