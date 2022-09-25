from contextlib import suppress

import pytest

from page_objects.login_page import LoginPage
from utilities.driver_manager import DriverWrapper
from utilities.project_logger import set_logger
from utilities.read_run_settings import ReadConfig
import allure


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def driver_wrapper_setup(request):
    DriverWrapper.create_driver(1, True)
    DriverWrapper.get_driver().maximize_window()
    set_logger()
    yield
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(DriverWrapper.get_driver().get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    DriverWrapper.shutdown()


@pytest.fixture()
def open_login_page(driver_wrapper_setup):
    DriverWrapper.get_driver().get(ReadConfig.get_application_url())
    return LoginPage()


# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def setup(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())
#     elif browser == 'firefox':
#         driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#     else: default_browser_will_be_here
#     return driver

# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'PET AUTOMATION'
    config._metadata['Module Name'] = 'TEST_MODULE'
    config._metadata['Tester'] = 'Bohdan Dovbysh'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
