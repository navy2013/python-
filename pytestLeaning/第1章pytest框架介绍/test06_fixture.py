import pytest
#如果@pytest.fixture()里面没有参数，那么默讣 scope=”function”，也就是此时的级别的 function，针对函数有效

@pytest.fixture()
def login():
    print("输入账号，密码先登录")


def test_s1(login):
    print("用例1：登录之后其它动作111")


def test_s2():
    print("用例2：不需要登录，操作222")


def test_s3(login):
    print("用例3：登录之后其它动作333")


if __name__ == '__main__':
    pytest.main(["-s", "test06_fixture"])
