from appium import webdriver
from helpers.config import *


def before_all(context):
    context.driver = webdriver.Remote(APPIUM_HOST, DESIRED_CAPS)


def after_all(context):
    context.driver.quit()
