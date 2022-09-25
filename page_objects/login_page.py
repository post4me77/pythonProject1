from selenium.webdriver.common.by import By

from page_objects.home_page import HomePage
from utilities.decorators import auto_steps
from utilities.web_ui.base_page import BasePage
from utilities.web_ui.ui_object import WebElement
from utilities.project_logger import logger


@auto_steps
class LoginPage(BasePage):
    _email_input = WebElement(By.XPATH, "//input[@id='Email']")
    _password_input = WebElement(By.ID, 'Password')
    _login_button = WebElement(By.XPATH, "//button[@type='submit']")

    def set_user_name(self, username):
        self._email_input.set_text(text=username)
        logger.info(f'Set email to {username}')

    def set_password(self, password):
        self._password_input.set_text(text=password)
        logger.info(f'Set password to {password}')

    def click_login(self) -> HomePage:
        self._login_button.click()
        logger.info(f'Click login button')
        return HomePage()

    def get_title(self):
        return self.get_actual_title()

    def login_to_app(self, user_name, password):
        self.set_user_name(user_name)
        self.set_password(password)
        self.click_login()
        logger.info(f'Login to app')
        return HomePage()
