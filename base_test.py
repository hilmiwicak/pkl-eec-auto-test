import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import constant


class BaseTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def setUp(self):
        chrome_service = Service(constant.DRIVER_PATH)
        chrome_option = Options()
        chrome_option.binary_location = constant.CHROME_PATH
        chrome_option.add_argument(constant.CHROME_DATA)
        chrome_option.add_argument("--ignore-gpu-blocklist")
        chrome_option.add_experimental_option(
            'excludeSwitches', ['enable-logging'])

        self.driver = webdriver.Chrome(options=chrome_option, service=chrome_service)
        self.driver.implicitly_wait(5)
        self.maxDiff = None

    def tearDown(self):
        self.driver.close()
