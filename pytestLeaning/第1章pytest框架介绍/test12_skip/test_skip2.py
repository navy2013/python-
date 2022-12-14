import pytest

"""
    除了通过使用标签的方式，还可以在测试用例中调用pytest.skip()方法来实现跳过，可以选择传入reason参数来说明跳过原因；
    如果想要通过判断是否跳过，可以写在if判断里（_）
"""


class TestClass():
    def test001(self):
        if 'h' in 'hell':
            pytest.skip(reason="跳过，不执行")  # 不执行后面的代码
            print("test001")

    def test002(self):
        print("test002")


if __name__ == '__main__':
    pytest.main(["-vs", "test.skip2.py"])
