import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By as SeleniumBy
from selenium.webdriver import Keys as SeleniumKeys
from selenium.webdriver.support.select import Select as SeleniumSelect
from selenium.common.exceptions import NoSuchElementException

import constant
import util


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.time = time
        self.constant = constant
        self.util = util
        self.By = SeleniumBy
        self.Keys = SeleniumKeys
        self.Select = SeleniumSelect
        self.NoSuchElementException = NoSuchElementException

    def open_home(self):
        self.driver.get(self.constant.BASE_URL + "/home")

    def click_submit_button_primary(self):
        button = self.driver.find_element(
            self.By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
        button.location_once_scrolled_into_view
        button.click()

    def get_message(self):
        return self.driver.find_element(
            self.By.CSS_SELECTOR, "span[data-notify='message']").text

    def get_data_table_empty(self):
        try:
            return self.driver.find_element(
                self.By.CSS_SELECTOR, "td.dataTables_empty").text
        except self.NoSuchElementException:
            return ""
