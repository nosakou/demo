from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def do_swipe(context):
    size = context.driver.get_window_size()
    startx, starty = int(size['width']) * 0.7, int(size['height']) * 0.5
    endx, endy = int(size['width']) * 0.1, int(size['height']) * 0.5
    context.driver.swipe(startx, starty, endx, endy, 300)


def assert_element_displayed(context, element):
    try:
        WebDriverWait(context.driver, 120).until(
            EC.presence_of_element_located(element)
        )
        assert context.driver.find_element(*element).is_displayed() is True
    except AssertionError as error:
        error.args += ('Element is not displayed')
        raise


def assert_element_has_text(context, element, text=None):
    try:
        WebDriverWait(context.driver, 120).until(
            EC.presence_of_element_located(element)
        )
        assert text in context.driver.find_element(*element).text
        return context.driver.find_element(*element)
    except AssertionError as error:
        error.args += ('Element doesn\'t have relevant text')
        raise
