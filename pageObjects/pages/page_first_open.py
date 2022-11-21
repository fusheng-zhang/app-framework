from ..basePage import BasePage
from ..locators.locator_first_open import FirstOpenPageLocators


class FirstOpenPage(BasePage):
    # 继承的：BasePage是我的父类，父类中的所有方法我都能用。

    def permission_allowandok(self):
        BasePage.click_thing(self, FirstOpenPageLocators.btn_ok)
        BasePage.click_thing(self, FirstOpenPageLocators.btn_ok)
        BasePage.click_thing(self, FirstOpenPageLocators.permission_allow)
