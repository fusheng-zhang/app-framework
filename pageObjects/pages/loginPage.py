from ..basePage import BasePage
from ..locators.loginLocators import LoginLocators


class LoginPage(BasePage):
    # 继承的：BasePage是我的父类，父类中的所有方法我都能用。

    def click_login_button(self):
        BasePage.click_thing(self, LoginLocators.button_login)
 

