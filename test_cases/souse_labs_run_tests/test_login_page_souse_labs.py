import allure

from utilities.assertions import Assertions


class TestLoginPageSouseLabsExample:

    @allure.feature('Login page test')
    def _test_home_page_title_passed(self, open_login_page_virtual):
        """
        ** Test Description **: test verifies title of login page on SouseLabsEnv

        ** Pre-conditions ** : Login page is opened

        ** Steps **
            1. Get title og Login Page

        ** Expected **
            1. Title is : Your store. Login
        """

        login_page = open_login_page_virtual
        assertion = Assertions()
        title = login_page.get_title()
        assertion.assert_with_screenshot(actual=title, expected="Your store. Login",
                                         message=f"\ntitle is incorrect\nActual: {title}\nExpected: Your store. Login")

    @allure.feature('Login page test')
    def _test_home_page_title_faied(self, open_login_page_virtual):
        """
        ** Test Description **: test verifies title of login page on SouseLabsEnv

        ** Pre-conditions ** : Login page is opened

        ** Steps **
            1. Get title og Login Page

        ** Expected **
            1. Title is : Your store. Login
        """

        login_page = open_login_page_virtual
        assertion = Assertions()
        title = login_page.get_title()
        assertion.assert_with_screenshot(actual=title, expected="FAILDE",
                                         message=f"\ntitle is incorrect\nActual: {title}\nExpected: Your store. Login")
