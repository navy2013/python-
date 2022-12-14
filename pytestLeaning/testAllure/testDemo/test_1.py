# import pytest
from funcDemo.Calc import Calc


class TestClass():
    def setup_method(self):
        print("setup-------------start")

    def setup_class(self):
        print("setup_class--------start")

    def test001(self):
        c = Calc()
        a = c.add(2, 3)
        assert a == -20

    def test002(self):
        c = Calc()
        a = c.subtract(2, 3)
        assert a == 5

    def test003(self):
        c = Calc()
        a = c.subtract(2, 6)
        assert a == 5

    def teardown_method(self):
        print("teardown---------end")

    def teardown_class(self):
        print("teardown_class-------end")


# if __name__ == '__main__':
#     pytest.main(["test_1.py"])
    # pytest.main(["--html=./report.html","test_1.py::TestClass::test003"])
