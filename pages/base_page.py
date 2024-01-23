import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By as SeleniumBy
from selenium.webdriver import Keys as SeleniumKeys
from selenium.webdriver.support.select import Select as SeleniumSelect

import constant


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.time = time
        self.constant = constant
        self.By = SeleniumBy
        self.Keys = SeleniumKeys
        self.Select = SeleniumSelect

    def open_home(self):
        self.driver.get(self.constant.BASE_URL + "/home")

    def click_submit_button_primary(self):
        button = self.driver.find_element(
            self.By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
        button.location_once_scrolled_into_view
        button.click()
