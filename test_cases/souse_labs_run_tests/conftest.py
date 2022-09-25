import os

import pytest

from page_objects.login_page import LoginPage
from utilities.driver_manager import DriverWrapper
from utilities.read_run_settings import ReadConfig


@pytest.fixture()
def create_souse_labs_driver(request):
    test_name = request.node.name
    souse_labs_configs = ReadConfig.get_souse_labs_configuration()
    capabilities = {
        "platformName": souse_labs_configs['platformname'],
        "browserName": souse_labs_configs['browsername'],
        "platformVersion": souse_labs_configs['platformversion'],
        "sauce:options": {
            "extendedDebugging": bool(souse_labs_configs['extendeddebugging']),
            "name": test_name
        }
    }
    _credentials = os.environ["SAUCE_USERNAME"] + ":" + os.environ["SAUCE_ACCESS_KEY"]
    _url = f"https://{_credentials}@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    driver = DriverWrapper.create_remote_driver(_url, capabilities)
    yield driver
    sauce_result = "failed" if request.node.rep_call.failed else "passed"  # added
    driver.execute_script("sauce:job-result={}".format(sauce_result))
    DriverWrapper.shutdown()


@pytest.fixture()
def open_login_page_virtual(create_souse_labs_driver):
    DriverWrapper.get_driver().get(ReadConfig.get_application_url())
    return LoginPage()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # this sets the result as a test attribute for Sauce Labs reporting.
    outcome = yield
    rep = outcome.get_result()

    # set an report attribute for each phase of a call
    setattr(item, "rep_" + rep.when, rep)

