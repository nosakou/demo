from selenium.webdriver.common.by import By
from config import BUNDLE_NAME


class MainPageLocators(object):
    ONBOARDING_PAGE = (By.ID, '%s:id/onboardingPageImage' % BUNDLE_NAME)
    BEGIN_BUTTON = (By.ID, '%s:id/beginButton' % BUNDLE_NAME)

