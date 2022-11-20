from datetime import datetime

import allure
import pytest
import yaml

from pageObjects.pages.loginPage import LoginPage
from utils.get_path import PATH


@allure.feature("登录功能")
class TestLoginPytest(object):
    @allure.step("初始化，打开手机，同意权限")
    @pytest.fixture(scope='module', autouse=True)
    def agree_init(self, run_app):
        # 初始化driver，文件级通用
        # 先初始化页面，
        ok = LoginPage.click_login_button(run_app)
        # 操作的方法
        ok.permission_allowandok()

    @allure.story("点击登录")
    @pytest.mark.regression
    @allure.severity("critical")
    # @pytest.mark.parametrize("add",
    #                          yaml.safe_load(open(PATH("../Testdatas/" + "addnotedata.yaml"), 'r', encoding='utf8')))
    def test_login(self, run_app):
        # 初始化登录页
        with allure.step("初始化添加页面"):
            login = LoginPage.LoginPage(run_app)
        # # 点击登录
        login.click_login_button()
        # # 截图
        login.save_pic(PATH("../reports/screenShots/" + str(datetime.now())) + "login.png")

    @pytest.mark.sanity
    # @pytest.mark.skip
    def test_deletenote(self):
        pass


if __name__ == '__main__':
    pytest.main()
