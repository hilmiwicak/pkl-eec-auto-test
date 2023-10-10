import unittest
import sys
import time

import constant
import util

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select


def ignore_warning():
    if not sys.warnoptions:
        import warnings
        warnings.simplefilter("ignore")


class eec_authentication_login(unittest.TestCase):

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

    # @unittest.skip # type: ignore #no reason needed
    def test_login(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "input.form-control[type='email']").send_keys("admin@eecid.com")
        self.driver.find_element(
            By.CSS_SELECTOR, "input.form-control[type='password']").send_keys("secret")
        self.driver.find_element(
            By.CSS_SELECTOR, "button.btn[type='submit']").click()

        # assert the next page have the word "Dashboard admin"
        cur_url = self.driver.current_url
        self.assertEqual(cur_url, constant.BASE_URL + "/home")
        # self.assertEqual(cur_url, constant.BASE_URL + "/")

    def tearDown(self):
        self.driver.close()


class eec_authentication_logout(unittest.TestCase):

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

    # @unittest.skipIf(test_login, "test_login is running")
    def test_logout(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link#navbarDropdownProfile").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "a.dropdown-item[href='" + constant.BASE_URL + "/logout']").click()

        cur_url = self.driver.current_url
        self.assertEqual(cur_url, constant.BASE_URL + "/login")

    def tearDown(self):
        self.driver.delete_cookie("eecid_session")
        self.driver.delete_cookie("XSRF-TOKEN")
        self.driver.close()


class eec_admin_account_management(unittest.TestCase):

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

    def test_account_verify(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/userManagement']").click()
        self.driver.get(constant.BASE_URL + "/userManagement")
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "button.btn-warning").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()

        # assert if the page have the word "User Approved"
        time.sleep(5)
        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "User Approved")

    def test_account_delete(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/userManagement']").click()
        time.sleep(1)
        self.driver.find_elements(
            By.CSS_SELECTOR, "button.btn-danger")[1].click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()

        # assert if the page have the word "User Deleted"
        time.sleep(5)
        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "Data Deleted!")

    def tearDown(self):
        self.driver.close()


class eec_admin_expert_management(unittest.TestCase):

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

    def test_expert_view(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/expertManagement']").click()
        time.sleep(1)

        tr = self.driver.find_elements(By.CSS_SELECTOR, "tr")
        self.assertGreater(len(tr), 1)

    def test_expert_add_not_eec(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/expertManagement']").click()
        # add_element = self.driver.find_element(
        #     By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/expertManagement']")
        # self.driver.execute_script("arguments[0].click();", add_element)
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "a.btn-primary").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "#name").send_keys("Test Name")
        self.driver.find_element(
            By.CSS_SELECTOR, "#nip").send_keys(util.random_nip_16())
        self.driver.find_element(
            By.CSS_SELECTOR, "#expert_company").send_keys("Test Company")
        self.driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']").click()
        self.driver.switch_to.alert.accept()

        time.sleep(5)
        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "Data Created!")

    def test_expert_add_eec(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/expertManagement']").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "a.btn-primary").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "#name").send_keys("Test Name")
        self.driver.find_element(
            By.CSS_SELECTOR, "#nip").send_keys(util.random_nip_11())
        self.driver.find_element(By.CSS_SELECTOR, "#eec_expert").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']").click()
        self.driver.switch_to.alert.accept()

        time.sleep(5)
        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "Data Created!")

    def test_expert_edit(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/expertManagement']").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "a.btn.btn-warning").click()
        time.sleep(1)
        name_input_element = self.driver.find_element(
            By.CSS_SELECTOR, "#name")
        name_input_element.send_keys(Keys.CONTROL, 'a')
        name_input_element.send_keys(Keys.DELETE)
        name_input_element.send_keys("Test Name")

        nip_input_element = self.driver.find_element(
            By.CSS_SELECTOR, "#nip")
        nip_input_element.send_keys(Keys.BACKSPACE)
        nip_input_element.send_keys("1")

        self.driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']").click()
        self.driver.switch_to.alert.accept()

        time.sleep(5)
        self.assertEqual(self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text, "Data Updated!")

    def test_expert_delete(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/expertManagement']").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-danger").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()

        time.sleep(5)
        self.assertEqual(self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text, "Data Deleted!")

    def tearDown(self):
        self.driver.close()


class eec_admin_site_radar_management(unittest.TestCase):

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

    def test_site_view(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/site']").click()
        time.sleep(1)

        card_list = self.driver.find_elements(
            By.CSS_SELECTOR, ".row .col-lg-4.col-md-6.col-sm-6")
        self.assertGreater(len(card_list), 0)

    def tearDown(self):
        self.driver.close


class eec_admin_distribution_management(unittest.TestCase):

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

    def test_distribution_view(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/distribution']").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "a.btn.btn-info").click()
        time.sleep(1)

        tr = self.driver.find_elements(By.CSS_SELECTOR, "tr")
        self.assertGreater(len(tr), 1)

    def test_distribution_add(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/distribution']").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "a.btn.btn-info").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary").click()

        time.sleep(1)
        distribution_sel_element = self.driver.find_element(By.ID, "site_id")
        distribution_sel = Select(distribution_sel_element)
        distribution_sel.select_by_index(1)

        distribution_expert_element = self.driver.find_element(
            By.ID, "expert_id")
        distribution_expert = Select(distribution_expert_element)
        distribution_expert.select_by_visible_text("Test Name")

        self.driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']").click()
        self.driver.switch_to.alert.accept()

        time.sleep(5)
        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "Data Created!")

    def test_distribution_edit(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/distribution']").click()
        time.sleep(1)
        self.driver.find_elements(
            By.CSS_SELECTOR, "a.btn.btn-info")[1].click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "a.btn.btn-warning").click()

        time.sleep(1)
        distribution_expert_element = self.driver.find_element(
            By.ID, "expert_id")
        distribution_expert = Select(distribution_expert_element)
        distribution_expert.select_by_visible_text("Test Name")

        self.driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']").click()
        self.driver.switch_to.alert.accept()

        time.sleep(5)
        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "Data Updated!")

    def test_distribution_delete(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/distribution']").click()
        time.sleep(1)
        self.driver.find_elements(
            By.CSS_SELECTOR, "a.btn.btn-info")[1].click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-danger").click()
        self.driver.switch_to.alert.accept()

        time.sleep(5)
        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "Data Deleted!")

    def tearDown(self):
        self.driver.close()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(eec_authentication_login("test_login"))

    # suite.addTest(eec_admin_account_management("test_account_verify"))
    # suite.addTest(eec_admin_account_management("test_account_delete"))

    # suite.addTest(eec_admin_expert_management("test_expert_add_not_eec"))
    # suite.addTest(eec_admin_expert_management("test_expert_add_eec"))
    # suite.addTest(eec_admin_expert_management("test_expert_view"))
    # suite.addTest(eec_admin_expert_management("test_expert_edit"))
    # suite.addTest(eec_admin_expert_management("test_expert_delete"))

    suite.addTest(eec_admin_site_radar_management("test_site_view"))

    # suite.addTest(eec_admin_distribution_management("test_distribution_view"))
    # suite.addTest(eec_admin_distribution_management("test_distribution_add"))
    # suite.addTest(eec_admin_distribution_management("test_distribution_edit"))
    # suite.addTest(eec_admin_distribution_management(
    #     "test_distribution_delete"))

    suite.addTest(eec_authentication_logout("test_logout"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
