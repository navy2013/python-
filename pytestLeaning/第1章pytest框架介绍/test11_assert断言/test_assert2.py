# 异常信息
def f():
    return 3


def test_function():
    a = f()
    assert a % 2 == 0, "判断a为偶数，当前a的值为：%s" % a

# E       AssertionError: 判断a为偶数，当前a的值为：3