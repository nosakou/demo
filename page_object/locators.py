from selenium.webdriver.common.by import By
from config import BUNDLE_NAME


class MainPageLocatorsAndroid(object):
    ONBOARDING_PAGE = (By.ID, '%s:id/onboardingPageTitle' % BUNDLE_NAME)
    BEGIN_BUTTON = (By.ID, '%s:id/beginButton' % BUNDLE_NAME)


class MainPageLocatorsIOS(object):
    ALLOW = (By.ID, 'Allow')
    BEGIN_BUTTON = (By.ID, 'Продолжить')
    TEXTS = [
        (By.ID, 'Покупайте авиабилеты быстрее, чем за 2 минуты'),
        (By.ID, 'Регистрируйтесь на рейс меньше, чем за 49 секунд'),
        (By.ID, 'Печатайте посадочные билеты с помощью терминалов в аэропорту'),
        (By.ID, 'Следите за мильным балансом')
    ]
