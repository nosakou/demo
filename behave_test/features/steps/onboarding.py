from behave import *
from behave_test.features.helpers.locators import *
from behave_test.features.helpers.utils import *

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
        'Регистрируйтесь куда угодно',
        'Печатайте постеры как угодно',
        'Делитесь чем угодно'
    ]
    for text in texts:
        do_swipe(context)
        assert_element_has_text(context, ONBOARD_TITLE, text=text)


@then("user sees finish button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_element_displayed(context, BEGIN_BUTTON).click()
