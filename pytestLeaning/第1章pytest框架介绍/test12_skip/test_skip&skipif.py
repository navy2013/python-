import pytest

"""
我们想要某个方法或跳过某条用例，在方法上加以下3种都可以

@pytest.mark.skip() 　　#1、跳过方法或用例，未备注原因

@pytest.mark.skip(reason='跳过一个方法或一个测试用例') 　　#2、跳过方法或用例，备注了原因

@pytest.mark.skipif(1==1,reason='跳过一个方法或一个测试用例')  　　 #3、当条件满足，跳过方法或用例，备注了原因
"""


class TestClass():
    """跳过方法，未备注原因"""

    @pytest.mark.skip()
    def test_one(self):
        print("test_one")

    """跳过方法，并备注原因"""

    @pytest.mark.skip(reason="跳过有原因")
    def test_two(self):
        print("test_two")

    """当条件满足时，跳过方法，并备注原因"""

    @pytest.mark.skipif(1 == 1, reason="条件成立时，跳过有原因")
    def test_three(self):
        print("test_three")


if __name__ == '__main__':
    pytest.main(["-vs", "test_skip&skipif.py"])
