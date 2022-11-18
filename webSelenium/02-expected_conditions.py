import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestECExample(object):

    def setup_class(self):
        print("set up")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.url = 'http://www.baidu.com'
        self.driver.get(self.url)

    def teardown_class(self):
        print("tear down")
        self.driver.quit()

    def test_01_title_is(self):
        '''判断title是否符合预期'''
        title_is_baidu = EC.title_is('百度一下，你就知道')
        assert title_is_baidu(self.driver)

    def test_02_title_contains(self):
        '''判断title是否包含预期字符'''
        title_should_contains_baidu = EC.title_contains('百度')
        assert title_should_contains_baidu(self.driver)

    def test_03_presence_of_elment_located(self):
        '''判断element是否出现在dom树'''
        locator = (By.ID, 'kw')
        search_text_field_should_present = EC.visibility_of_element_located(locator)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        ele = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 10).until(EC.visibility_of(ele))
        assert search_text_field_should_present(self.driver)

    def test_04_visibility_of(self):
        search_text_field = self.driver.find_element(By.ID, 'kw')
        search_text_field_should_visible = EC.visibility_of(search_text_field)
        assert search_text_field_should_visible(self.driver)

    def test_05_text_to_be_present_in_element(self):
        text_should_present = EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#s-top-left > a:nth-child(2)'), 'hao123')
        assert text_should_present(self.driver)


if __name__ == '__main__':
    pytest.main(['-sv', '02-expected_conditions.py'])
