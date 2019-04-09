*** Settings ***
Documentation    On Boarding
Variables    test_variables.py
Resource  resource.robot
Test Setup  Open Application  ${APPIUM_HOST}
                   ...   deviceName=${DEVICE_NAME}
                   ...   app=${APP}
                   ...   platformName=${PLATFORM_NAME}
                   ...   platformVersion=${PLATFORM_VERSION}
Test Teardown  Close Application


*** Keywords ***
Be sure you see the begin button
    Wait Until Element Is Visible    id=${ONBOARDING_PAGE}
    :FOR  ${TEXT}  IN  @{ONBOARD_TEXTS}
    \    Element Should Contain Text   id=${ONBOARDING_PAGE}   ${TEXT}
    \    Do Swipe
    Wait Until Element Is Visible    id=${BEGIN_BUTTON}
    Click Element    id=${BEGIN_BUTTON}


*** Test Cases ***
Demo
    [Tags]  OnBoarding
    Be sure you see the begin button
