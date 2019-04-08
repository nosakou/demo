from .locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def do_swipe(self):
        size = self.driver.get_window_size()
        startx, starty = int(size['width']) * 0.8, int(size['height']) * 0.5
        endx, endy = int(size['width']) * 0.2, int(size['height']) * 0.5
        self.driver.swipe(startx, starty, endx, endy, 300)

    def assert_element_displayed(self, element):
        try:
            WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located(element)
            )
            assert self.driver.find_element(*element).is_displayed() is True
        except AssertionError as error:
            error.args += ('Element is not displayed')
            raise

    def assert_element_has_text(self, element, text=None):
        try:
            WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located(element)
            )
            assert text in self.driver.find_element(*element).text
            return self.driver.find_element(*element)
        except AssertionError as error:
            error.args += ('Element is not displayed')
            raise


class MainPage(BasePage):

    locators = MainPageLocators()

    def click_finish(self):
        element = self.driver.find_element(
            *self.locators.BEGIN_BUTTON
        )
        element.click()
