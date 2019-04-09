from appium import webdriver
from page import MainPage
from config import DESIRED_CAPS_ANDROID, DESIRED_CAPS_IOS, APPIUM_HOST


class TestAndroid:

    def setup_class(self):
        self.driver = webdriver.Remote(APPIUM_HOST, DESIRED_CAPS_ANDROID)

    def teardown_class(self):
        self.driver.quit()

    def test_onboarding_android(self):
        onboarding_texts = [
            'Покупайте авиабилеты быстрее, чем за 2 минуты',
            'Регистрируйтесь на рейс меньше, чем за 49 секунд',
            'Печатайте посадочные билеты с помощью терминалов в аэропорту',
            'Следите за бонусным балансом'
        ]
        main_page = MainPage(self.driver, platform='android')
        for text in onboarding_texts:
            main_page.do_swipe()
            main_page.assert_element_displayed(main_page.locators.ONBOARDING_PAGE)
            main_page.assert_element_has_text(main_page.locators.ONBOARDING_PAGE, text)
        main_page.assert_element_displayed(main_page.locators.BEGIN_BUTTON)


class TestIOS:
    def setup_class(self):
        self.driver = webdriver.Remote(APPIUM_HOST, DESIRED_CAPS_IOS)

    def teardown_class(self):
        self.driver.quit()

    def test_onboarding_ios(self):

        main_page = MainPage(self.driver, platform='ios')
        main_page.assert_element_displayed(main_page.locators.ALLOW).click()
        texts = main_page.locators.TEXTS

        for text in texts:
            main_page.assert_element_displayed(text)
            main_page.do_swipe()
        main_page.assert_element_displayed(main_page.locators.BEGIN_BUTTON)
