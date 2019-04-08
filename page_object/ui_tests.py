from appium import webdriver
from .page import MainPage
from .config import DESIRED_CAPS, APPIUM_HOST


class TestUM:

    def setup_class(self):
        self.driver = webdriver.Remote(APPIUM_HOST, DESIRED_CAPS)

    def teardown_class(self):
        self.driver.quit()

    def test_onboarding(self):
        onboarding_texts = [
            'Регистрируйтесь на концерт меньше, чем за 69 секунд',
            'Печатайте постеры с помощью терминалов в аэропорту',
            'Слушайте музыку, оставляйте комментарии'
        ]
        main_page = MainPage(self.driver)
        for text in onboarding_texts:
            main_page.do_swipe()
            main_page.assert_element_displayed(main_page.locators.ONBOARDING_PAGE)
            main_page.assert_element_has_text(main_page.locators.ONBOARDING_PAGE, text)
        main_page.assert_element_displayed(main_page.locators.BEGIN_BUTTON)
