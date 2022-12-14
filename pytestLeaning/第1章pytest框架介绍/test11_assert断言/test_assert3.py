import pytest


# 异常断言

def test_zero_division():
    '''断言异常'''
    with pytest.raises(ZeroDivisionError) as excinfo:
        1 / 0

    # 断言异常类型 type
    assert excinfo.type == ZeroDivisionError

    # 断言异常value值
    assert "division by zero" in str(excinfo.value)
