from selenium.webdriver.common.by import By
from config import BUNDLE_NAME


# группа локаторов онбординга
ONBOARD_TITLE = (By.ID, '%s:id/onboardingPageTitle' % BUNDLE_NAME)
BEGIN_BUTTON = (By.ID, '%s:id/beginButton' % BUNDLE_NAME)
