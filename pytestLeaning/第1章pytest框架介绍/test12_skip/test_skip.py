import pytest

# 1、@pytest.mark.skip()被标记的类中所有方法测试用例都会被跳过

@pytest.mark.skip(reason='跳过TestSkip类中的所有方法')
class TestSkip(object):
    def test01(self):
        print("test01")
        assert 1 == 1

    def test02(self):
        print("test02")
        assert 1 == 1


if __name__ == '__main__':
    pytest.main(["-vs", "test_skip.py"])
