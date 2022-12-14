import pytest

"""2、被标记的类，当条件为ture时，会被跳过，否则不跳过

　　2.1 被标记的类，当条件成立时，会跳过类中的所有方法
"""


@pytest.mark.skipif(1 == 1, reason="当条件成立，跳过类中的所有方法")
class TestSkipif():
    def test03(self):
        print("test03")
        assert 3 == 3

    def test04(self):
        print("test04")
        assert 4 == 4


if __name__ == '__main__':
    pytest.main(["-rs", "test_skipif.py"])
