from appium.webdriver.common.mobileby import MobileBy


class FirstOpenPageLocators(object):
    btn_ok = (MobileBy.ID, "com.youdao.note:id/btn_ok")
    permission_allow = (MobileBy.ID, "com.lbe.security.miui:id/permission_allow_foreground_only_button")