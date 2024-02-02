import unittest
import sys

from selenium.webdriver.common.by import By

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

        # with self.subTest("invalid email and password"):
        #     login_page.login("wrong_email@email.com", "wrong password")
        #
        #     message = self.driver.find_element(By.ID, "email-error").text
        #     self.assertEqual(message, "These credentials do not match our records.")

        with self.subTest("valid email and password"):
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

        with self.subTest("1. different current password, and confirmation password, valid new"):
            profile_page.edit_password(
                "wrong password", "wrong password", "wrong password1")

            message_current = profile_page.get_message_current_password_error()
            message_new = profile_page.get_message_new_password_error()
            self.assertEqual(
                message_current, "The current password field does not match your password")
            self.assertEqual(
                message_new, "The password confirmation does not match.")

        with self.subTest("2. current password less than 6 characters, new password less than 6 characters, same password confirmation"):
            profile_page.edit_password("wrong", "wrong", "wrong")

            message_current = profile_page.get_message_current_password_error()
            message_new = profile_page.get_message_new_password_error()
            self.assertEqual(
                message_current, "The current password must be at least 6 characters.")
            self.assertEqual(
                message_new, "The password must be at least 6 characters.")

        with self.subTest("3. empty"):
            profile_page.edit_password("", "", "")

            message_current = profile_page.get_message_current_password_error()
            message_new = profile_page.get_message_new_password_error()
            self.assertEqual(
                message_current, "The current password field is required.")
            self.assertEqual(message_new, "The password field is required.")

        with self.subTest("4. same new password"):
            profile_page.edit_password(
                constant.PASSWORD, constant.PASSWORD, constant.PASSWORD)

            message_new = profile_page.get_message_new_password_error()
            self.assertEqual(
                message_new, "The password and current password must be different.")

        with self.subTest("5. valid password"):
            profile_page.edit_password(
                constant.PASSWORD, constant.NEW_PASSWORD, constant.NEW_PASSWORD)

            message = profile_page.get_message()
            self.assertEqual(message, "Password has succesfully changed!")

        # outside skripsi
        with self.subTest("revert the password"):
            profile_page.edit_password(
                constant.NEW_PASSWORD, constant.PASSWORD, constant.PASSWORD)

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

    def test_add_expert(self):
        expert_page = ExpertPage(self.driver)
        nip_eec_expert = util.random_nip_11()

        with self.subTest("1. name more than 15, nip less than 11, valid company"):
            expert_page.add_expert(
                "this name is more than 15", util.random_nip_lt_11(), "Test Company")

            message_name = expert_page.get_message_name_error()
            message_nip = expert_page.get_message_nip_error()
            message_company = expert_page.get_message_company_error()
            self.assertEqual(
                message_name, "The name may not be greater than 15 characters.")
            self.assertEqual(
                message_nip, "This input must be 11 or 18 digits.")
            self.assertEqual(message_company, "")

        with self.subTest("2. name not regular string, nip not integer, expert company not regular string"):
            expert_page.add_expert("Björk 东-л", "test 10000.0", "компанија-測試")

            message_name = expert_page.get_message_name_error()
            message_nip = expert_page.get_message_nip_error()
            message_company = expert_page.get_message_company_error()
            self.assertEqual(message_name, "")
            self.assertEqual(
                message_nip, "This input must be 11 or 18 digits.")
            self.assertEqual(message_company, "")

        with self.subTest("3. correct name, nip more than 18 digit, eec expert"):
            expert_page.add_expert(constant.EXPERT_NAME,
                                   util.random_nip_gt_18())

            message_name = expert_page.get_message_name_error()
            message_nip = expert_page.get_message_nip_error()
            message_company = expert_page.get_message_company_error()
            self.assertEqual(message_name, "")
            self.assertEqual(
                message_nip, "This input must be 11 or 18 digits.")
            self.assertEqual(message_company, "")

        # ERROR
        with self.subTest("4. correct name, correct eec company, nip 18 digit"):
            expert_page.add_expert("Test Name", util.random_nip_18())

            message_name = expert_page.get_message_name_error()
            message_nip = expert_page.get_message_nip_error()
            message_company = expert_page.get_message_company_error()
            self.assertEqual(message_name, "")
            self.assertEqual(message_nip, "something")
            self.assertEqual(message_company, "")

        with self.subTest("5. empty"):
            expert_page.add_expert("", "", "")

            message_name = expert_page.get_message_name_error()
            message_nip = expert_page.get_message_nip_error()
            message_company = expert_page.get_message_company_error()
            self.assertEqual(message_name, "The name field is required.")
            self.assertEqual(message_nip, "The nip field is required.")
            self.assertEqual(
                message_company, "The expert company field is required.")

        with self.subTest("6. correct inputs, not eec expert"):
            expert_page.add_expert(
                "Test Not EEC", util.random_nip_18(), "Test Company")

            message = expert_page.get_message()
            self.assertEqual(message, "Data Created!")

        with self.subTest("7. correct inputs, eec expert"):
            expert_page.add_expert(constant.EXPERT_NAME, nip_eec_expert)

            message = expert_page.get_message()
            self.assertEqual(message, "Data Created!")

        # ERROR
        with self.subTest("8. same name, same nip, eec expert"):
            expert_page.add_expert(constant.EXPERT_NAME, nip_eec_expert)

            message_name = expert_page.get_message_name_error()
            message_nip = expert_page.get_message_nip_error()
            message_company = expert_page.get_message_company_error()
            self.assertEqual(message_name, "")
            self.assertEqual(message_nip, "The nip has already been taken.")
            self.assertEqual(message_company, "")

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
        site_radar_stock_page.edit_site_stock("Test Sited Stock Name Edit", util.random_part_number(
        ), util.random_serial_number(), "10162023", "11262023")

        message = site_radar_stock_page.get_message()
        self.assertEqual(message, "Data Edited!")

    def test_delete_site_stock(self):
        site_radar_stock_page = SiteRadarStockPage(self.driver)
        site_radar_stock_page.delete_site_stock()

        message = site_radar_stock_page.get_message()
        self.assertEqual(message, "Data Deleted!")


class StockManagement(BaseTest):

    def test_view_stock(self):
        stock_page = StockPage(self.driver)
        stock_page.view_stock()

        tr = self.driver.find_elements(By.CSS_SELECTOR, "tr")
        self.assertGreater(len(tr), 0)

    def test_add_stock(self):
        stock_page = StockPage(self.driver)
        stock_page.add_stock("Test New Item Stock", util.random_part_number(
        ), util.random_serial_number(), "10162023", "11162023", "1", "Keterangan Test Item")

        message = stock_page.get_message()
        self.assertEqual(message, "Data berhasil ditambah!")

    def test_edit_stock(self):
        stock_page = StockPage(self.driver)
        stock_page.edit_stock()

        message = stock_page.get_message()
        self.assertEqual(message, "Data berhasil di update")

    def test_delete_stock(self):
        stock_page = StockPage(self.driver)
        stock_page.delete_stock()

        message = stock_page.get_message()
        self.assertEqual(message, "Data berhasil di hapus")

    def test_view_stock_recommendation(self):
        stock_page = StockPage(self.driver)
        stock_page.view_stock_recommendation()

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
    suite.addTest(ExpertManagement("test_add_expert"))
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

    # suite.addTest(SiteRadarStockManagement(
    #     "test_view_site_stock"))
    # suite.addTest(SiteRadarStockManagement("test_add_site_stock"))
    # suite.addTest(SiteRadarStockManagement(
    #     "test_edit_site_stock"))
    # suite.addTest(SiteRadarStockManagement(
    #     "test_delete_site_stock"))

    # suite.addTest(StockManagement("test_view_stock"))
    # suite.addTest(StockManagement("test_add_stock"))
    # suite.addTest(StockManagement("test_edit_stock"))
    # suite.addTest(StockManagement("test_delete_stock"))
    # suite.addTest(StockManagement("test_view_stock_recommendation"))

    suite.addTest(AuthenticationLogout("test_logout"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
