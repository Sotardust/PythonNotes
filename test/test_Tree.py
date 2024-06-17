import allure
import pytest
from api.shoping_api import ApiCase
from data_driver import yaml_driver


@allure.epic("shopXo电商平台接口-接口测试")
class TestTree:
    # 初始化用例库
    actions1 = ApiCase()

    @allure.feature("01.登陆")
    @allure.story("02.一般场景")
    @pytest.mark.parametrize('userdata', yaml_driver.load_yaml('../yaml/user.yaml'))
    def test_case01(self, userdata):
        self.actions1.params_login(userdata)

    @allure.feature("02.个人查询")
    @allure.story("01.典型场景")
    @allure.title("个人查询")
    def test_case02(self, token_fix):
        self.actions1.params_getuserinfo(token_fix)

    @allure.feature("03.添加商品到购物车")
    @allure.story("01.典型场景")
    @allure.title("添加商品到购物车")
    def test_case03(self, token_fix):
        self.actions1.params_addcart(token_fix)

    @allure.feature("04.下单")
    @allure.story("01.典型场景")
    @allure.title("下单")
    def test_case04(self, token_fix):
        self.actions1.params_createorder(token_fix)
