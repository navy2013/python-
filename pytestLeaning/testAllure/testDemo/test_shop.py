import allure
import pytest
import os





class TestShop():
    @allure.feature("购物车")  # 用于描述被测试产品需求 1
    @allure.story("商品展示")  # 用于描述feature的用户场景，即测试需求 2
    def test_show(self):
        with allure.step("用户登录"):  # 用于描述测试步骤，将会输出到报告中
            allure.attach("jack", "用户名")  # 用于向测试报告中输入一些附加的信息，通常是一些测试数据，截图等

        with allure.step("查看商品信息"):
            allure.attach("H7", "哈弗")

    @allure.feature("购物车")
    @allure.story("商品添加")
    def test_add(self):
        print("添加----add")
        assert 1 == 0

    @allure.feature("购物车")
    @allure.story("商品删除")
    def test_delete(self):
        print("删除")


if __name__ == '__main__':
    pytest.main(["--alluredir", "report/result", "test_shop.py"])  # 生成报告json
    # 将测试报告转为html格式
    cmd = "allure" + "generate" + "./report/result" + "-o" + "./report/html" + "--clean"
    os.system(cmd)
