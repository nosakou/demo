APPIUM_HOST = 'http://localhost:4723/wd/hub'

MY_APP_ANDROID = '14022019.apk'
MY_APP_IOS = 'inhouse.app'

DESIRED_CAPS_ANDROID = {
    'platformName': 'Android',
    'platformVersion': '7.1',
    'deviceName': 'Android Emulator',
    'app': MY_APP_ANDROID
}

BUNDLE_NAME = 'ru.bundle.some'

DESIRED_CAPS_IOS = {
    'platformName': 'iOS',
    'platformVersion': '12.1',
    'deviceName': 'iPhone 6',
    'app': MY_APP_IOS
}