import pytest
from appium import webdriver

from utils.desired_caps import get_desired_caps
from utils.get_path import PATH
from utils.get_yaml import get_yaml_data


@pytest.fixture(scope="session")
def run_app(request):
    desired_cap_value = get_desired_caps()
    driver = webdriver.Remote(
        get_yaml_data(PATH("../config/conf.yaml"))["base_url"], desired_cap_value
    )
    driver.implicitly_wait(15)

    def close_app():
        driver.quit()

    request.addfinalizer(close_app)
    return driver
