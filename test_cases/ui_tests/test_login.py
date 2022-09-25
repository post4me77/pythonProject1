import allure

from utilities.assertions import Assertions
from utilities.read_run_settings import ReadConfig
from utilities.waiters import wait_until


@allure.feature('Login page test')
def test_home_page_title(open_login_page):
    """
    ** Test Description **: test verifies title of login page

    ** Pre-conditions ** : Login page is opened

    ** Steps **
        1. Get title og Login Page

    ** Expected **
        1. Title is : Your store. Login
    """
    login_page = open_login_page
    title = login_page.get_title()
    assert title == "Your store. Login"
    # assertion.assert_with_screenshot(actual=title, expected="Your store. Login",
    #                                  message=f"\ntitle is incorrect\nActual: {title}\nExpected: Your store. Login")


@allure.feature('Login page test')
def test_login(open_login_page):
    """
        ** Test Description **: test verifies thar user can login to application

        ** Pre-conditions ** : Login page is opened

        ** Steps **
            1. Enter valid email
            2. Enter valid password
            3. Click Login button

        ** Expected **
            1. User login to application
    """
    expected_title = "Dashboard / nopCommerce administration"
    login_page = open_login_page
    # assertion = Assertions()
    home_page = login_page.login_to_app(user_name=ReadConfig.get_user_email(),
                                        password=ReadConfig.get_password())
    wait_until(lambda: home_page.get_title() == expected_title, f'Page title is not as expected')
    page_title = home_page.get_title()
    assert page_title == expected_title
    # assertion.assert_with_screenshot(actual=page_title, expected=expected_title,
    #                                  message=f"\ntitle is incorrect\nActual: {page_title}"
    #                                          f"\nExpected: Dashboard / nopCommerce administration")
