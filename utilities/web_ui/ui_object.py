import time

from selenium.webdriver import ActionChains

from utilities.driver_manager import DriverWrapper
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class WebElement:
    def __init__(self, by, locator):
        self.by = by
        self.locator = locator

    def get_element(self, timeout=10):
        # self.wait_to_appear(timeout)
        return DriverWrapper.get_driver().find_element(self.by, self.locator)

    def get_all_elements(self, timeout=10):
        self.wait_to_appear(timeout)
        return DriverWrapper.get_driver().find_elements(self.by, self.locator)

    def get_locator(self):
        return self.locator

    def get_text(self):
        return self.get_element().text

    def get_attribute(self, value):
        return self.get_element().get_attribute(value)

    def is_selected(self):
        return self.get_element().is_selected()

    def is_checked(self):
        return DriverWrapper.get_driver().execute_script("return arguments[0].checked", self.get_element())

    def is_exist(self):
        try:
            WebDriverWait(DriverWrapper.get_driver(), 1).until(EC.presence_of_element_located((self.by, self.locator)))
        except:
            return False

    def is_clickable(self):
        try:
            WebDriverWait(DriverWrapper.get_driver(), 1).until(EC.element_to_be_clickable((self.by, self.locator)))
        except:
            return False

    def wait_to_be_clickable(self, timeout=10):
        WebDriverWait(DriverWrapper.get_driver(), timeout).until(EC.element_to_be_clickable((self.by, self.locator)))

    def wait_to_appear(self, timeout=10, ignore_error=False):
        start = time.time()
        while (time.time() - start) < timeout:
            if self.is_exist():
                return self
        if not ignore_error:
            raise TimeoutError(f"Locator {self.locator} does not exists in DOM after {timeout} seconds")
        else:
            return self

    def click(self, timeout=10, use_action_chains=False, is_wait_for_clickable=True):
        if is_wait_for_clickable:
            self.wait_to_be_clickable(timeout)
        if use_action_chains:
            element = self.get_element(timeout)
            ActionChains(DriverWrapper.get_driver()).move_to_element(element).click().perform()
        else:
            self.get_element(timeout).click()

    def set_text(self, text):
        self.get_element().clear()
        self.get_element().send_keys(text)

    def type_text(self, text):
        self.get_element().send_keys(text)

