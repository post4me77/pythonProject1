import inspect
import allure

from utilities.driver_manager import DriverWrapper
from allure_commons.types import AttachmentType


class Assertions:
    def __init__(self):
        self.driver = DriverWrapper.get_driver()

    @allure.step
    def assert_with_screenshot(self, actual, expected, message):
        allure.attach(self.driver.get_screenshot_as_png(), name=f"{inspect.stack()[1][3]}",
                      attachment_type=AttachmentType.PNG)
        assert actual == expected, message
