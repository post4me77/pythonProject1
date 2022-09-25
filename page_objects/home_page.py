import allure
from selenium.webdriver.common.by import By

from utilities.web_ui.base_page import BasePage
from utilities.web_ui.ui_object import WebElement


class HomePage(BasePage):
    _logout_link_text = WebElement(By.LINK_TEXT, "Logout")

    @allure.step
    def click_logout(self):
        self._logout_link_text.click()

    @allure.step
    def get_title(self):
        return self.get_actual_title()

    # @allure.step
    # def get_navigation_menu(self):
    #     return NavigationMenu()
    #
