import unittest
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

import constant
import util


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

    def test_login(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "input.form-control[type='email']").send_keys("admin@eecid.com")
        self.driver.find_element(
            By.CSS_SELECTOR, "input.form-control[type='password']").send_keys("secret")
        button = self.driver.find_element(
            By.CSS_SELECTOR, "button.btn[type='submit']")
        button.location_once_scrolled_into_view
        button.click()

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
        self.driver.quit()


class eec_admin_management(unittest.TestCase):

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

    def test_admin_password_edit(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link#navbarDropdownProfile").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "a.dropdown-item[href='" + constant.BASE_URL + "/profile']").click()

        time.sleep(1)
        self.driver.find_element(
            By.ID, "input-current-password").send_keys("secret")
        self.driver.find_element(
            By.ID, "input-password").send_keys("secret1")
        self.driver.find_element(
            By.ID, "input-password-confirmation").send_keys("secret1")

        button = self.driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
        button.location_once_scrolled_into_view
        button.click()

        time.sleep(5)
        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "Password has succesfully changed!")

    def tearDown(self):
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

        time.sleep(5)
        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "Data Deleted!")

    def tearDown(self):
        self.driver.close()


class eec_admin_maintenance_management(unittest.TestCase):

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

    def test_pm_view(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/expertActivity']").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "a.btn-info[href='" + constant.BASE_URL + "/pm']").click()

        time.sleep(1)
        tr = self.driver.find_elements(By.CSS_SELECTOR, "tr")
        self.assertGreater(len(tr), 1)

    def test_pm_detail_view(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/expertActivity']").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "a.btn-info[href='" + constant.BASE_URL + "/pm']").click()

        time.sleep(1)
        self.driver.find_elements(
            By.CSS_SELECTOR, "a.btn.btn-info")[1].click()

        time.sleep(1)
        site = self.driver.find_elements(By.CSS_SELECTOR, "h4.card-title")[1].text
        self.assertIsNotNone(site)

    def test_cm_detail_view(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/expertActivity']").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "a.btn-info[href='" + constant.BASE_URL + "/cm']").click()

        time.sleep(1)
        self.driver.find_elements(
            By.CSS_SELECTOR, "a.btn.btn-info")[1].click()

        time.sleep(1)
        site = self.driver.find_elements(By.CSS_SELECTOR, "h4.card-title")[1].text
        self.assertIsNotNone(site)

    def test_cm_view(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/expertActivity']").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "a.btn-info[href='" + constant.BASE_URL + "/cm']").click()

        time.sleep(1)
        tr = self.driver.find_elements(By.CSS_SELECTOR, "tr")
        self.assertGreater(len(tr), 1)

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
            By.ID, "name").send_keys("Test Name")
        self.driver.find_element(
            By.ID, "nip").send_keys(util.random_nip_16())
        self.driver.find_element(
            By.ID, "expert_company").send_keys("Test Company")
        button = self.driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
        button.location_once_scrolled_into_view
        button.click()
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
            By.ID, "name").send_keys("Test Name")
        self.driver.find_element(
            By.ID, "nip").send_keys(util.random_nip_11())
        self.driver.find_element(By.ID, "eec_expert").click()
        button = self.driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
        button.location_once_scrolled_into_view
        button.click()
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
            By.ID, "name")
        name_input_element.clear()
        name_input_element.send_keys("Test Name")

        nip_input_element = self.driver.find_element(
            By.ID, "nip")
        nip_input_element.send_keys(Keys.BACKSPACE)
        nip_input_element.send_keys("1")

        button = self.driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
        button.location_once_scrolled_into_view
        button.click()
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

    def test_site_add(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/site']").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "a.btn-primary").click()
        time.sleep(1)
        self.driver.find_element(
            By.ID, "radar_name").send_keys("Test Radar Site")
        self.driver.find_element(
            By.ID, "station_id").send_keys("Test Location")
        self.driver.find_element(By.ID, "image").send_keys(
            r"C:\Users\Hilmi\dev-projects\skripsi-selenium\skripsi-src\resources\radar.jpeg")

        stock_site_element = self.driver.find_element(
            By.CSS_SELECTOR, "select.form-control.site")
        stock_site_select = Select(stock_site_element)
        stock_site_select.select_by_index(1)

        button = self.driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
        button.location_once_scrolled_into_view
        button.click()
        self.driver.switch_to.alert.accept()

        time.sleep(5)
        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "Data Created!")

    def test_site_delete(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/site']").click()
        time.sleep(1)
        card_element = self.driver.find_element(
            By.XPATH, "//strong[contains(text(),'Test Location')]/ancestor::div[contains(@class, 'card card-stats')]")
        card_element.find_element(
            By.XPATH, "//button[contains(@class, 'btn-danger')]").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()

        time.sleep(5)
        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "Data Deleted!")

    def tearDown(self):
        self.driver.close()


class eec_admin_site_radar_stock_management(unittest.TestCase):

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

    def test_site_stock_view(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/site']").click()
        time.sleep(1)
        card_element = self.driver.find_element(
            By.XPATH, "//strong[contains(text(),'Test Location')]/ancestor::div[contains(@class, 'card card-stats')]")
        a_element = card_element.find_element(
            By.XPATH, ".//a[contains(@class, 'btn-info')]")
        a_element.location_once_scrolled_into_view
        a_element.click()

        time.sleep(5)
        tr_element = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        self.assertGreater(len(tr_element), 0)

    def test_site_stock_add(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/site']").click()
        time.sleep(1)
        card_element = self.driver.find_element(
            By.XPATH, "//strong[contains(text(),'Test Location')]/ancestor::div[contains(@class, 'card card-stats')]")
        a_element = card_element.find_element(
            By.XPATH, ".//a[contains(@class, 'btn-info')]")
        a_element.location_once_scrolled_into_view
        a_element.click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "a.btn-outline-primary.text-right").click()

        time.sleep(1)
        stock_sel_element_0 = self.driver.find_element(
            By.CSS_SELECTOR, "select[name='stocks[0][stock_id]']")
        stock_sel_0 = Select(stock_sel_element_0)
        stock_sel_0.select_by_index(1)

        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "button.btn-secondary").click()
        stock_sel_element_1 = self.driver.find_element(
            By.CSS_SELECTOR, "select[name='stocks[1][stock_id]']")
        stock_sel_1 = Select(stock_sel_element_1)
        stock_sel_1.select_by_index(2)

        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "button.btn-secondary").click()
        stock_sel_element_2 = self.driver.find_element(
            By.CSS_SELECTOR, "select[name='stocks[2][stock_id]']")
        stock_sel_2 = Select(stock_sel_element_2)
        stock_sel_2.select_by_index(3)

        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "button.btn-secondary").click()
        stock_sel_element_3 = self.driver.find_element(
            By.CSS_SELECTOR, "select[name='stocks[3][stock_id]']")
        stock_sel_3 = Select(stock_sel_element_3)
        stock_sel_3.select_by_index(4)

        button = self.driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
        button.location_once_scrolled_into_view
        button.click()

        time.sleep(5)
        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "Data Created!")

    def test_site_stock_edit(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/site']").click()
        time.sleep(1)
        card_element = self.driver.find_element(
            By.XPATH, "//strong[contains(text(),'Test Location')]/ancestor::div[contains(@class, 'card card-stats')]")
        a_element = card_element.find_element(
            By.XPATH, ".//a[contains(@class, 'btn-info')]")
        a_element.location_once_scrolled_into_view
        a_element.click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "a.btn-warning").click()

        time.sleep(1)
        name_input_element = self.driver.find_element(
            By.ID, "nama_barang")
        name_input_element.clear()
        name_input_element.send_keys("Test Stock Radar")

        self.driver.find_element(
            By.CSS_SELECTOR, "span.select2-selection__arrow").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "li[aria-selected='false']").click()

        part_number_element = self.driver.find_element(By.ID, "part_number")
        part_number_element.clear()
        part_number_element.send_keys(util.random_part_number())

        self.driver.find_element(By.ID, "serial_number").send_keys(
            util.random_serial_number())

        self.driver.find_element(By.ID, "tgl_masuk").send_keys("10162023")

        self.driver.find_element(By.ID, "expired").send_keys("11162023")

        button = self.driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
        button.location_once_scrolled_into_view
        button.click()

        time.sleep(5)
        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "Data Edited!")

    def test_site_stock_delete(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/site']").click()
        time.sleep(1)
        card_element = self.driver.find_element(
            By.XPATH, "//strong[contains(text(),'Test Location')]/ancestor::div[contains(@class, 'card card-stats')]")
        a_element = card_element.find_element(
            By.XPATH, ".//a[contains(@class, 'btn-info')]")
        a_element.location_once_scrolled_into_view
        a_element.click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "button.btn-danger").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()

        time.sleep(5)
        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "Data Deleted!")

    def tearDown(self):
        self.driver.close()


class eec_admin_stock_management(unittest.TestCase):

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

    def test_stock_view(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/stocks']").click()

        time.sleep(1)
        tr = self.driver.find_elements(By.CSS_SELECTOR, "tr")
        self.assertGreater(len(tr), 1)

    def test_stock_add(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/stocks']").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "a.btn-outline-primary[data-original-title='add item']").click()

        time.sleep(1)
        self.driver.find_element(By.ID, "nama_barang").send_keys(
            "Test Item Inventory")

        self.driver.find_element(
            By.CSS_SELECTOR, "span.select2-selection__arrow").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "li[aria-selected='false']").click()

        self.driver.find_element(By.ID, "part_number").send_keys(
            util.random_part_number())

        self.driver.find_element(By.ID, "ref_des").send_keys(
            util.random_serial_number())

        self.driver.find_element(By.ID, "tgl_masuk").send_keys("10162023")

        self.driver.find_element(By.ID, "expired").send_keys("11162023")

        self.driver.find_element(By.ID, "button_kurs_beli").click()

        self.driver.find_element(By.ID, "jumlah_unit").send_keys("1")

        stock_status_element = self.driver.find_element(By.ID, "status")
        stock_status_element.location_once_scrolled_into_view
        stock_status_select = Select(stock_status_element)
        stock_status_select.select_by_value("Obsolete")

        self.driver.find_element(By.ID, "keterangan").send_keys(
            "Keterangan Test Item")

        button_element = self.driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
        button_element.location_once_scrolled_into_view
        button_element.click()

        time.sleep(5)
        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "Data berhasil ditambah!")

    def test_stock_edit(self):
        # self.driver.get(constant.BASE_URL + "/home")
        # self.driver.find_element(
        #     By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/stocks']").click()
        self.driver.get(constant.BASE_URL + "/stocks")
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "a.btn.btn-warning").click()

        time.sleep(1)

        name_element = self.driver.find_element(By.ID, "nama_barang")
        name_element.clear()
        name_element.send_keys("Test Stock Edit")

        self.driver.find_element(
            By.CSS_SELECTOR, "span.select2-selection__arrow").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "li[aria-selected='false']").click()

        part_number_element = self.driver.find_element(By.ID, "part_number")
        part_number_element.clear()
        part_number_element.send_keys(util.random_part_number())

        ref_des_element = self.driver.find_element(By.ID, "ref_des")
        ref_des_element.clear()
        ref_des_element.send_keys(util.random_serial_number())

        self.driver.find_element(By.ID, "tgl_masuk").send_keys("10262023")

        expired_element = self.driver.find_element(By.ID, "expired")
        expired_element.location_once_scrolled_into_view
        expired_element.send_keys("11262023")

        unit_element = self.driver.find_element(By.ID, "jumlah_unit")
        unit_element.clear()
        unit_element.send_keys("2")

        stock_status_element = self.driver.find_element(By.ID, "status")
        stock_status_element.location_once_scrolled_into_view
        stock_status_select = Select(stock_status_element)
        stock_status_select.select_by_value("Dummy")

        description_element = self.driver.find_element(
            By.ID, "keterangan")
        description_element.location_once_scrolled_into_view
        description_element.clear()
        description_element.send_keys("Keterangan Test Stock Edit")

        button_element = self.driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
        button_element.location_once_scrolled_into_view
        button_element.click()

        time.sleep(5)
        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "Data berhasil di update")

    def test_stock_delete(self):
        # self.driver.get(constant.BASE_URL + "/home")
        # self.driver.find_element(
        #     By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/stocks']").click()
        self.driver.get(constant.BASE_URL + "/stocks")
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-danger").click()
        self.driver.switch_to.alert.accept()

        time.sleep(5)
        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "Data berhasil di hapus")

    def tearDown(self):
        self.driver.close()


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

    # suite.addTest(eec_admin_management("test_admin_password_edit"))

    # suite.addTest(eec_admin_account_management("test_account_verify"))
    # suite.addTest(eec_admin_account_management("test_account_delete"))

    # suite.addTest(eec_admin_expert_management("test_expert_view"))
    # suite.addTest(eec_admin_expert_management("test_expert_add_not_eec"))
    # suite.addTest(eec_admin_expert_management("test_expert_add_eec"))
    # suite.addTest(eec_admin_expert_management("test_expert_edit"))
    # suite.addTest(eec_admin_expert_management("test_expert_delete"))

    # suite.addTest(eec_admin_maintenance_management("test_pm_view"))
    # suite.addTest(eec_admin_maintenance_management("test_cm_view"))
    suite.addTest(eec_admin_maintenance_management("test_pm_detail_view"))
    suite.addTest(eec_admin_maintenance_management("test_cm_detail_view"))

    # suite.addTest(eec_admin_distribution_management("test_distribution_view"))
    # suite.addTest(eec_admin_distribution_management("test_distribution_add"))
    # suite.addTest(eec_admin_distribution_management("test_distribution_edit"))
    # suite.addTest(eec_admin_distribution_management(
    #     "test_distribution_delete"))

    # suite.addTest(eec_admin_site_radar_management("test_site_view"))
    # suite.addTest(eec_admin_site_radar_management("test_site_add"))
    # suite.addTest(eec_admin_site_radar_management("test_site_delete"))

    # suite.addTest(eec_admin_site_radar_stock_management(
    #     "test_site_stock_view"))
    # suite.addTest(eec_admin_site_radar_stock_management("test_site_stock_add"))
    # suite.addTest(eec_admin_site_radar_stock_management(
    #     "test_site_stock_edit"))
    # suite.addTest(eec_admin_site_radar_stock_management(
    #     "test_site_stock_delete"))

    # suite.addTest(eec_admin_stock_management("test_stock_view"))
    # suite.addTest(eec_admin_stock_management("test_stock_add"))
    # suite.addTest(eec_admin_stock_management("test_stock_edit"))
    # suite.addTest(eec_admin_stock_management("test_stock_delete"))

    suite.addTest(eec_authentication_logout("test_logout"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
