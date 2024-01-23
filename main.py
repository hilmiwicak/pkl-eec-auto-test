import unittest
import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

import constant
from base_test import BaseTest
from pages import *
import util


def ignore_warning():
    if not sys.warnoptions:
        import warnings
        warnings.simplefilter("ignore")


class AuthenticationLogin(BaseTest):

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login(constant.EMAIL, constant.PASSWORD)

        cur_url = self.driver.current_url
        self.assertEqual(cur_url, constant.BASE_URL + "/home")


class AuthenticationLogout(BaseTest):

    def test_logout(self):
        login_page = LoginPage(self.driver)
        login_page.logout()

        cur_url = self.driver.current_url
        self.assertEqual(cur_url, constant.BASE_URL + "/login")

    def tearDown(self):
        self.driver.delete_cookie("eecid_session")
        self.driver.delete_cookie("XSRF-TOKEN")
        self.driver.quit()


class PasswordEdit(BaseTest):

    def test_edit_password(self):
        profile_page = ProfilePage(self.driver)
        profile_page.edit_password(constant.PASSWORD, constant.NEW_PASSWORD)
        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "Password has succesfully changed!")


class AccountManagement(BaseTest):

    def test_verify_account(self):
        account_page = AccountPage(self.driver)
        account_page.verify_account()

        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "User Approved")

    def test_delete_account(self):
        account_page = AccountPage(self.driver)
        account_page.delete_account()

        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "Data Deleted!")


class MaintenanceManagement(BaseTest):

    def test_view_pm(self):
        pm_page = MaintenancePage(self.driver)
        pm_page.view_pm()

        tr = self.driver.find_elements(By.CSS_SELECTOR, "tr")
        self.assertGreater(len(tr), 1)

    def test_view_detail_pm(self):
        pm_page = MaintenancePage(self.driver)
        pm_page.view_detail_pm()

        site = self.driver.find_elements(
            By.CSS_SELECTOR, "h4.card-title")[1].text
        self.assertIsNotNone(site)

    def test_view_cm(self):
        cm_page = MaintenancePage(self.driver)
        cm_page.view_cm()

        tr = self.driver.find_elements(By.CSS_SELECTOR, "tr")
        self.assertGreater(len(tr), 1)

    def test_view_detail_cm(self):
        cm_page = MaintenancePage(self.driver)
        cm_page.view_detail_cm()

        site = self.driver.find_elements(
            By.CSS_SELECTOR, "h4.card-title")[1].text
        self.assertIsNotNone(site)


class ExpertManagement(BaseTest):

    def test_view_expert(self):
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


class SiteRadarManagement(BaseTest):

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


class SiteRadarStockManagement(BaseTest):

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
        tr = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        self.assertGreater(len(tr), 1)

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


class StockManagement(BaseTest):

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
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/stocks']").click()
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
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/stocks']").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "button.btn.btn-danger").click()
        self.driver.switch_to.alert.accept()

        time.sleep(5)
        message = self.driver.find_element(
            By.CSS_SELECTOR, "span[data-notify='message']").text
        self.assertEqual(message, "Data berhasil di hapus")

    def test_stock_recommendation_view(self):
        self.driver.get(constant.BASE_URL + "/home")
        self.driver.find_element(
            By.CSS_SELECTOR, "a.nav-link[href='" + constant.BASE_URL + "/stocks']").click()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, "a[data-original-title='recommendation item']").click()

        time.sleep(1)
        tr = self.driver.find_elements(By.CSS_SELECTOR, "tr")
        self.assertGreater(len(tr), 1)


class DistributionManagement(BaseTest):

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


def suite():
    suite = unittest.TestSuite()
    suite.addTest(AuthenticationLogin("test_login"))

    # suite.addTest(PasswordEdit("test_edit_password"))

    # suite.addTest(AccountManagement("test_verify_account"))
    # suite.addTest(AccountManagement("test_delete_account"))

    suite.addTest(MaintenanceManagement("test_view_pm"))
    suite.addTest(MaintenanceManagement("test_view_cm"))
    suite.addTest(MaintenanceManagement("test_view_detail_pm"))
    suite.addTest(MaintenanceManagement("test_view_detail_cm"))

    # suite.addTest(ExpertManagement("test_expert_view"))
    # suite.addTest(ExpertManagement("test_expert_add_not_eec"))
    # suite.addTest(ExpertManagement("test_expert_add_eec"))
    # suite.addTest(ExpertManagement("test_expert_edit"))
    # suite.addTest(ExpertManagement("test_expert_delete"))

    # suite.addTest(DistributionManagement("test_distribution_view"))
    # suite.addTest(DistributionManagement("test_distribution_add"))
    # suite.addTest(DistributionManagement("test_distribution_edit"))
    # suite.addTest(DistributionManagement(
    #     "test_distribution_delete"))

    # suite.addTest(SiteRadarManagement("test_site_view"))
    # suite.addTest(SiteRadarManagement("test_site_add"))
    # suite.addTest(SiteRadarManagement("test_site_delete"))

    # suite.addTest(SiteRadarStockManagement(
    #     "test_site_stock_view"))
    # suite.addTest(SiteRadarStockManagement("test_site_stock_add"))
    # suite.addTest(SiteRadarStockManagement(
    #     "test_site_stock_edit"))
    # suite.addTest(SiteRadarStockManagement(
    #     "test_site_stock_delete"))

    # suite.addTest(StockManagement("test_stock_view"))
    # suite.addTest(StockManagement("test_stock_add"))
    # suite.addTest(StockManagement("test_stock_edit"))
    # suite.addTest(StockManagement("test_stock_delete"))
    # suite.addTest(StockManagement("test_stock_recommendation_view"))

    suite.addTest(AuthenticationLogout("test_logout"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
