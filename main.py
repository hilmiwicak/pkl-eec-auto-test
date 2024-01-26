import unittest
import sys
import time

from selenium.webdriver.common.by import By
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

        message = profile_page.get_message()
        self.assertEqual(message, "Password has succesfully changed!")


class AccountManagement(BaseTest):

    def test_verify_account(self):
        account_page = AccountPage(self.driver)
        account_page.verify_account()

        message = account_page.get_message()
        self.assertEqual(message, "User Approved")

    def test_delete_account(self):
        account_page = AccountPage(self.driver)
        account_page.delete_account()

        message = account_page.get_message()
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
        expert_page = ExpertPage(self.driver)
        expert_page.view_expert()

        tr = self.driver.find_elements(By.CSS_SELECTOR, "tr")
        self.assertGreater(len(tr), 1)

    def test_add_not_eec_expert(self):
        expert_page = ExpertPage(self.driver)
        expert_page.add_not_eec_expert("Test Not EEC", util.random_nip_18(), "Test Company")

        message = expert_page.get_message()
        self.assertEqual(message, "Data Created!")

    def test_add_eec_expert(self):
        expert_page = ExpertPage(self.driver)
        expert_page.add_eec_expert(constant.EXPERT_NAME, util.random_nip_11())

        message = expert_page.get_message()
        self.assertEqual(message, "Data Created!")

    def test_edit_expert(self):
        expert_page = ExpertPage(self.driver)
        expert_page.edit_expert("Test Name Edit", util.random_nip_18())

        message = expert_page.get_message()
        self.assertEqual(message, "Data Updated!")

    def test_delete_expert(self):
        expert_page = ExpertPage(self.driver)
        expert_page.delete_expert()

        message = expert_page.get_message()
        self.assertEqual(message, "Data Deleted!")


class DistributionManagement(BaseTest):

    def test_view_distribution(self):
        distribution_page = DistributionPage(self.driver)
        distribution_page.view_distribution()

        tr = self.driver.find_elements(By.CSS_SELECTOR, "tr")
        self.assertGreater(len(tr), 1)

    def test_add_distribution(self):
        distribution_page = DistributionPage(self.driver)
        distribution_page.add_distribution(constant.EXPERT_NAME)

        message = distribution_page.get_message()
        self.assertEqual(message, "Data Created!")

    def test_edit_distribution(self):
        distribution_page = DistributionPage(self.driver)
        distribution_page.edit_distribution(constant.EXPERT_NAME)

        message = distribution_page.get_message()
        self.assertEqual(message, "Data Updated!")

    def test_delete_distribution(self):
        distribution_page = DistributionPage(self.driver)
        distribution_page.delete_distribution()

        message = distribution_page.get_message()
        self.assertEqual(message, "Data Deleted!")


class SiteRadarManagement(BaseTest):

    def test_view_site(self):
        site_radar_page = SiteRadarPage(self.driver)
        site_radar_page.view_site()

        card_list = self.driver.find_elements(
            By.CSS_SELECTOR, ".row .col-lg-4.col-md-6.col-sm-6")
        self.assertGreater(len(card_list), 0)

    def test_add_site(self):
        site_radar_page = SiteRadarPage(self.driver)
        site_radar_page.add_site()

        message = site_radar_page.get_message()
        self.assertEqual(message, "Data Created!")

    def test_delete_site(self):
        site_radar_page = SiteRadarPage(self.driver)
        site_radar_page.delete_site()

        message = site_radar_page.get_message()
        self.assertEqual(message, "Data Deleted!")


class SiteRadarStockManagement(BaseTest):

    def test_view_site_stock(self):
        site_radar_stock_page = SiteRadarStockPage(self.driver)
        site_radar_stock_page.view_site_stock()

        tr = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        self.assertGreater(len(tr), 0)

    def test_add_site_stock(self):
        site_radar_stock_page = SiteRadarStockPage(self.driver)
        site_radar_stock_page.add_site_stock()

        message = site_radar_stock_page.get_message()
        self.assertEqual(message, "Data Created!")

    def test_edit_site_stock(self):
        site_radar_stock_page = SiteRadarStockPage(self.driver)
        site_radar_stock_page.edit_site_stock()

        message = site_radar_stock_page.get_message()
        self.assertEqual(message, "Data Edited!")

    def test_delete_site_stock(self):
        site_radar_stock_page = SiteRadarStockPage(self.driver)
        site_radar_stock_page.delete_site_stock()

        message = site_radar_stock_page.get_message()
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


def suite():
    suite = unittest.TestSuite()
    suite.addTest(AuthenticationLogin("test_login"))

    # suite.addTest(PasswordEdit("test_edit_password"))

    # suite.addTest(AccountManagement("test_verify_account"))
    # suite.addTest(AccountManagement("test_delete_account"))

    # suite.addTest(MaintenanceManagement("test_view_pm"))
    # suite.addTest(MaintenanceManagement("test_view_cm"))
    # suite.addTest(MaintenanceManagement("test_view_detail_pm"))
    # suite.addTest(MaintenanceManagement("test_view_detail_cm"))

    # suite.addTest(ExpertManagement("test_view_expert"))
    # suite.addTest(ExpertManagement("test_add_not_eec_expert"))
    # suite.addTest(ExpertManagement("test_add_eec_expert"))
    # suite.addTest(ExpertManagement("test_edit_expert"))
    # suite.addTest(ExpertManagement("test_delete_expert"))

    # suite.addTest(DistributionManagement("test_view_distribution"))
    # suite.addTest(DistributionManagement("test_add_distribution"))
    # suite.addTest(DistributionManagement("test_edit_distribution"))
    # suite.addTest(DistributionManagement(
    #     "test_delete_distribution"))

    # suite.addTest(SiteRadarManagement("test_view_site"))
    # suite.addTest(SiteRadarManagement("test_add_site"))
    # suite.addTest(SiteRadarManagement("test_delete_site"))

    suite.addTest(SiteRadarStockManagement(
        "test_view_site_stock"))
    suite.addTest(SiteRadarStockManagement("test_add_site_stock"))
    suite.addTest(SiteRadarStockManagement(
        "test_edit_site_stock"))
    suite.addTest(SiteRadarStockManagement(
        "test_delete_site_stock"))

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
