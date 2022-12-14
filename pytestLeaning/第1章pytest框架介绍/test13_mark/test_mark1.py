import pytest
import os,sys

@pytest.mark.web
def test_send_http():
    pass


def test_something_quick():
    pass


def test_another():
    pass


class TestClass:
    def test_method(self):
        pass


if __name__ == '__main__':
    pytest.main(['-s', '-m="web"', 'test_mark1.py'])
    # pytest.main(["-v", "test_mark1.py::TestClass::test_method"])
    # os.system("pytest -v test_mark1.py::TestClass::test_method")