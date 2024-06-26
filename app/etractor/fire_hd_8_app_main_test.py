# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import unittest

import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
options.load_capabilities({
    "appium:platformName": "Android",
    "appium:platformVersion": "11",
    "appium:deviceName": "Genymobile Fire HD 8",
    "appium:appPackage": "com.aiforcetech.etractor",
    "appium:appActivity": ".SplashActivity",
    "appium:noReset": True,
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:automationName": "UiAutomator2",
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})


# driver.quit()


class TestAppium:

    def test_find_battery(self):
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
        # driver.activate_app("com.aiforcetech.etractor")
        el = driver.find_element(by=AppiumBy.XPATH,
                                 value='//android.widget.ImageView[@resource-id="com.aiforcetech.etractor:id/menuButton"]')
        el.click()


if __name__ == '__main__':
    pytest.main(['-s', __file__])
