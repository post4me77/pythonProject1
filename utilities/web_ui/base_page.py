from utilities.decorators import auto_steps
from utilities.driver_manager import DriverWrapper
import allure


@auto_steps
class BasePage:

    @allure.step
    def get_actual_url(self):
        return DriverWrapper.get_driver().current_url

    @allure.step
    def get_actual_title(self):
        return DriverWrapper.get_driver().title
