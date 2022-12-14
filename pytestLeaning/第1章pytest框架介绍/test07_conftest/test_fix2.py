import pytest


def test_s4(login):
    print("用例4：登录之后其它动作444")


def test_s5():
    print("用例5：不需要登录，操作555")


if __name__ == '__main__':
    pytest.main(["-s", "test_fix2"])

# 单独运行 test_fix1.py 呾 test_fix2.py 都能调用到 login()方法，
# 返样就能实现一些公共的操作可以单独拿出来了
