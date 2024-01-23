import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import constant


class BaseTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def setUp(self):
        service_obj = Service(constant.DRIVER_PATH)
        chrome_opt = Options()
        chrome_opt.binary_location = constant.CHROME_PATH
        chrome_opt.add_argument(constant.CHROME_DATA)
        chrome_opt.add_argument("--ignore-gpu-blocklist")
        chrome_opt.add_experimental_option(
            'excludeSwitches', ['enable-logging'])

        self.driver = webdriver.Chrome(options=chrome_opt, service=service_obj)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.close()
