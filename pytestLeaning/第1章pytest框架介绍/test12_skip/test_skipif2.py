import pytest

"""
2.2 被标记的类，当条件不成立时，不会跳过类中的所有方法
"""


@pytest.mark.skipif(1 == 3, reason="当条件不成立，不跳过类中的所有方法")
class TestSkipif():
    def test03(self):
        print("test03")
        assert 3 == 3

    def test04(self):
        print("test04")
        assert 4 == 4


if __name__ == '__main__':
    pytest.main(["-rs", "test_skipif.py"])
