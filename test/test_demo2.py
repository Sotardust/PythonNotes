import pytest


class TestDome:

    def test_demo1(self):
        print('--测试用例执行-------------')
        assert 11 == 11

    def test_Demo(self):
        assert 21 == 21


if __name__ == '__main__':
    pytest.main(['-s', __file__])
