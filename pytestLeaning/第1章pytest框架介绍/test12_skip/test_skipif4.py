import pytest

"""
    类中条件不满足，方法中条件也不满足，不跳过继续执行
    类中条件不满足，方法中条件满足，跳过不执行
"""


@pytest.mark.skipif(1 == 2, reason="条件不满足，不跳过")
class TestClass():
    @pytest.mark.skip(reason="跳过不执行")
    def test1(self):
        print("test1")

    @pytest.mark.skipif(1 == 1, reason="条件满足，跳过不执行")
    def test2(self):
        print("test2")

    @pytest.mark.skipif(1 == 2, reason="条件不满足，不跳过，继续执行")
    def test3(self):
        print("test3")


if __name__ == '__main__':
    pytest.main(["-vs", "test_skipif4.py"])
