import pytest
import allure

from utilities.assertions import Assertions
from utilities.project_logger import logger
from utilities.xls_parser import *


class TestDDTLogin:
    test_data_path = r'../../test_data/login_data.xlsx'

    @pytest.mark.regression
    @allure.feature("TEST DDT")
    def _test_login_ddt(self, open_login_page):
        logger.info(f"{'*' * 10}{self.test_login_ddt.__name__} START {'*' * 10}")
        login_page = open_login_page
        assertion = Assertions()

        self.rows = get_row_count(self.test_data_path, 'Sheet1')
        for r in range(2, self.rows + 1):
            self.user = read_data(self.test_data_path, 'Sheet1', r, 1)
            self.password = read_data(self.test_data_path, 'Sheet1', r, 2)
            self.exp = read_data(self.test_data_path, 'Sheet1', r, 3)

            login_page.set_user_name(self.user)
            login_page.set_password(self.password)
            home_page = login_page.click_login()

            act_title = home_page.get_actual_title()
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    home_page.click_logout()
                    result = "Pass"
                elif self.exp == 'Fail':
                    home_page.click_logout()
                    result = "Fail"
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    result = "Pass"
                elif self.exp == 'Fail':
                    result = "Fail"
            assertion.assert_with_screenshot(actual=result, expected=self.exp,
                                             message=f"\ntitle is incorrect\nActual: {result}\nExpected: {self.exp}")

        logger.info(f"{'*' * 10}{self.test_login_ddt.__name__} FINISHED {'*' * 10}")
