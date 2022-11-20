from utils.get_path import PATH


def get_desired_caps():
    desired_caps = {
        "platformName": "android",
        "deviceName": "Fusheng",
        "platformVersion": "12.0",
        # "app": PATH("../app/test.apk"),
        # "unicodeKeyboard": True,
        # "resetKeyboard":False,
    }
    return desired_caps
