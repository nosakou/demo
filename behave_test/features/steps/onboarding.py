from behave import *
from behave_test.features.helpers.utils import *
from behave_test.features.helpers.locators import *

use_step_matcher("re")


@given("activity started normally")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.driver
    assert_element_displayed(context, ONBOARD_TITLE)


@then("user swipes on-boarding")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    texts = [
        'Покупайте авиабилеты быстрее, чем за 2 минуты',
        'Регистрируйтесь на рейс меньше, чем за 49 секунд',
        'Печатайте посадочные билеты с помощью терминалов в аэропорту',
        'Следите за бонусным балансом'
    ]
    for text in texts:
        assert_element_has_text(context, ONBOARD_TITLE, text=text)
        do_swipe(context)


@then("user sees begin button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_element_displayed(context, BEGIN_BUTTON).click()
