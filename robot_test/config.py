APPIUM_HOST = 'http://localhost:4723/wd/hub'
DEVICE_NAME = 'EMULATOR'
BUNDLE = 'ru.some.bundle'
APP = 'some.apk'
PLATFORM_NAME = 'Android'
PLATFORM_VERSION = '7.1'
ONBOARDING_PAGE = '%s:id/onboardingPageTitle' % BUNDLE
BEGIN_BUTTON = '%s:id/beginButton' % BUNDLE
ONBOARD_TEXTS = [
    'Покупайте авиабилеты быстрее, чем за 29 минуты',
    'Регистрируйтесь на рейс меньше, чем за 49 секунд',
    'Печатайте посадочные билеты с помощью терминалов в аэропорту',
    'Следите за бонусным балансом'
]
