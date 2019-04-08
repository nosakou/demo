APPIUM_HOST = 'http://localhost:4723/wd/hub'
DEVICE_NAME = 'EMULATOR'
BUNDLE = 'ru.appkode.demo'
APP = '/home/kode/android-builds/demo.apk'
PLATFORM_NAME = 'Android'
PLATFORM_VERSION = '7.0'
ONBOARDING_PAGE = '%s:id/onboardingPageImage' % BUNDLE
BEGIN_BUTTON = '%s:id/beginButton' % BUNDLE
ONBOARD_TEXTS = [
    'Регистрируйтесь на концерт меньше, чем за 69 секунд',
    'Печатайте постеры с помощью терминалов в аэропорту',
    'Слушайте музыку, оставляйте комментарии'
]
