import pytest


def test_s1(login):
    print("用例1：登录之后其它动作111")


def test_s2():
    print("用例2：不需要登录，操作222")


def test_s3(login):
    print("用例3：登录之后其它动作333")


if __name__ == '__main__':
    pytest.main(["-s", "test_fix1"])

# 单独运行 test_fix1.py 呾 test_fix2.py 都能调用到 login()方法，
# 返样就能实现一些公共的操作可以单独拿出来了