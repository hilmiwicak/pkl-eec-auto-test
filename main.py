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
        #     message = self.driver.find_element("email-error").text
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

        with self.subTest("5. new password not regular string"):
            profile_page.edit_password(
                constant.PASSWORD, constant.NEW_PASSWORD, constant.NEW_PASSWORD)

            message = profile_page.get_message()
            self.assertEqual(message, "Password has succesfully changed!")

        # ERROR
        with self.subTest("6. current password not regular string"):
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

        table_empty = pm_page.get_data_table_empty()
        self.assertEqual(table_empty, "")

    def test_view_detail_pm(self):
        pm_page = MaintenancePage(self.driver)
        pm_page.view_detail_pm()

        site = self.driver.find_elements(
            By.CSS_SELECTOR, "h4.card-title")[1].text
        self.assertIsNotNone(site)

    def test_view_cm(self):
        cm_page = MaintenancePage(self.driver)
        cm_page.view_cm()

        table_empty = cm_page.get_data_table_empty()
        self.assertEqual(table_empty, "")

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

        table_empty = expert_page.get_data_table_empty()
        self.assertEqual(table_empty, "")

    def test_add_expert(self):
        expert_page = ExpertPage(self.driver)

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
            self.assertEqual(message_nip, "EEC Expert must have 11 digits.")
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
            expert_page.add_expert(constant.EXPERT_NAME, constant.EXPERT_NIP)

            message = expert_page.get_message()
            self.assertEqual(message, "Data Created!")

        # ERROR
        with self.subTest("8. same name, same nip, eec expert"):
            expert_page.add_expert(constant.EXPERT_NAME, constant.EXPERT_NIP)

            message_name = expert_page.get_message_name_error()
            message_nip = expert_page.get_message_nip_error()
            message_company = expert_page.get_message_company_error()
            self.assertEqual(message_name, "")
            self.assertEqual(message_nip, "The nip has already been taken.")
            self.assertEqual(message_company, "")

    def test_edit_expert(self):
        expert_page = ExpertPage(self.driver)

        name_view, nip_view, company_view = expert_page.view_expert_detail()
        name_edit, nip_edit, company_edit = expert_page.edit_expert_detail()

        self.assertEqual(name_view, name_edit)
        self.assertEqual(nip_view, nip_edit)
        self.assertEqual(company_view, company_edit)

    def test_delete_expert(self):
        expert_page = ExpertPage(self.driver)
        expert_page.delete_expert()

        message = expert_page.get_message()
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

        # ERROR
        with self.subTest("1. radar name not regular string, site location not regular string, image not image, stock select on but not selecting"):
            site_radar_page.add_site(
                "⽗⾇!-?2", "⽗⾇!-?2", "", constant.SITE_VIDEO_PATH)

            message_radar_name = site_radar_page.get_message_radar_name_error()
            message_station_id = site_radar_page.get_message_station_id_error()
            message_stock = site_radar_page.get_message_stock_error()
            message_image = site_radar_page.get_message_image_error()
            self.assertEqual(message_radar_name, "")
            self.assertEqual(message_station_id, "")
            self.assertEqual(message_stock, "This field is required")
            self.assertEqual(message_image, "The image must be an image.")

        # ERROR
        with self.subTest("2. empty inputs, not selecting stocks"):
            site_radar_page.add_site("", "", "delete", "")

            message_radar_name = site_radar_page.get_message_radar_name_error()
            message_station_id = site_radar_page.get_message_station_id_error()
            message_stock = site_radar_page.get_message_stock_error()
            message_image = site_radar_page.get_message_image_error()
            self.assertEqual(message_radar_name,
                             "The radar name field is required.")
            self.assertEqual(message_station_id,
                             "The station id field is required.")
            self.assertEqual(message_stock, "This field is required")
            self.assertEqual(message_image, "")

        with self.subTest("3. correct input stock select on but not selecting"):
            site_radar_page.add_site(
                constant.SITE_NAME, constant.SITE_LOCATION, "", constant.SITE_IMAGE_PATH)

            message_radar_name = site_radar_page.get_message_radar_name_error()
            message_station_id = site_radar_page.get_message_station_id_error()
            message_stock = site_radar_page.get_message_stock_error()
            message_image = site_radar_page.get_message_image_error()
            self.assertEqual(message_radar_name, "")
            self.assertEqual(message_station_id, "")
            self.assertEqual(message_stock, "This field is required")
            self.assertEqual(message_image, "")

        with self.subTest("4. correct inputs, stock not selecting"):
            site_radar_page.add_site(
                constant.SITE_NAME, constant.SITE_LOCATION, "delete", constant.SITE_IMAGE_PATH)

            message_radar_name = site_radar_page.get_message_radar_name_error()
            message_station_id = site_radar_page.get_message_station_id_error()
            message_stock = site_radar_page.get_message_stock_error()
            message_image = site_radar_page.get_message_image_error()
            self.assertEqual(message_radar_name, "")
            self.assertEqual(message_station_id, "")
            self.assertEqual(message_stock, "This field is required")
            self.assertEqual(message_image, "")

        with self.subTest("5. correct inputs with some stock"):
            site_radar_page.add_site(
                constant.SITE_NAME, constant.SITE_LOCATION, 1, constant.SITE_IMAGE_PATH)

            message = site_radar_page.get_message()
            self.assertEqual(message, "Data Created!")

        # outside skripsi
        # adds one more site for test_delete_site and SiteRadarStockManagement
        with self.subTest():
            site_radar_page.add_site(
                constant.SITE_NAME, constant.SITE_LOCATION, 1, constant.SITE_IMAGE_PATH)

            message = site_radar_page.get_message()
            self.assertEqual(message, "Data Created!")

    # dependent of add_site
    def test_delete_site(self):
        site_radar_page = SiteRadarPage(self.driver)
        site_radar_page.delete_site()

        message = site_radar_page.get_message()
        self.assertEqual(message, "Data Deleted!")


class DistributionManagement(BaseTest):

    def test_view_distribution(self):
        distribution_page = DistributionPage(self.driver)

        radar_name_view = distribution_page.view_distribution_list_radar_name()
        radar_name_detail = distribution_page.view_distribution_detail_radar_name()

        self.assertEqual(radar_name_view, radar_name_detail)

    # dependent of add_expert for subtest 2
    def test_add_distribution(self):
        distribution_page = DistributionPage(self.driver)

        with self.subTest("1. checking wheter the name in the view is not on the add form"):
            name_from_view, name_list_from_select_add = distribution_page.add_distribution_detail()

            self.assertNotIn(name_from_view, name_list_from_select_add)

        with self.subTest("2. empty inputs"):
            distribution_page.add_distribution("", "")

            message_site_id = distribution_page.get_message_site_id_error()
            message_expert_id = distribution_page.get_message_expert_id_error()
            self.assertEqual(message_site_id, "The site id field is required.")
            self.assertEqual(message_expert_id,
                             "The expert id field is required.")

        with self.subTest("3. correct inputs"):
            distribution_page.add_distribution(1, 1)

            message = distribution_page.get_message()
            self.assertEqual(message, "Data Created!")

        # outside skripsi
        # adds one more random expert distribution for test_delete_distribution and test_edit_distribution
        with self.subTest():
            distribution_page.add_distribution(1, 1)

            message = distribution_page.get_message()
            self.assertEqual(message, "Data Created!")

    def test_edit_distribution(self):
        distribution_page = DistributionPage(self.driver)

        with self.subTest("1. checking wheter the name in the view is not on the detail"):
            name_from_view, name_list_from_select_detail = distribution_page.edit_distribution_detail()

            self.assertNotIn(name_from_view, name_list_from_select_detail)

        with self.subTest("2. empty inputs"):
            distribution_page.edit_distribution("")

            message_expert_id = distribution_page.get_message_expert_id_error()
            self.assertEqual(message_expert_id,
                             "The expert id field is required.")

        with self.subTest("3. correct inputs"):
            distribution_page.edit_distribution(1)

            message = distribution_page.get_message()
            self.assertEqual(message, "Data Updated!")

    def test_delete_distribution(self):
        distribution_page = DistributionPage(self.driver)
        distribution_page.delete_distribution()

        message = distribution_page.get_message()
        self.assertEqual(message, "Data Deleted!")


class StockManagement(BaseTest):

    def test_view_stock(self):
        stock_page = StockPage(self.driver)
        stock_page.view_stock()

        table_empty = stock_page.get_data_table_empty()
        self.assertEqual(table_empty, "")

    def test_add_stock(self):
        stock_page = StockPage(self.driver)

        tgl_masuk_invalid, expired_invalid = util.random_invalid_tgl_masuk_and_expired()
        tgl_masuk_valid, expired_valid = util.random_valid_tgl_masuk_and_expired()

        with self.subTest("1. string inputs not regular characters, kurs beli not number, jumlah unit not integer, expired date before tgl masuk"):
            stock_page.add_stock(
                nama_barang="1-?ⴙ⺻✷⤵≣⼺⥊ⅿ⇆⌂⹁⊹⣁ⰴ⻏⥺⪈",
                group="1-?☉⛓∫ⰶ⦿ⶪ⪧⪪",
                part_number="PL-3-?ⶪ⪧⪪⼺⥊ⅿ⇆",
                ref_des="⽗⾇q?ⶪ⪧⪪⼺",
                tgl_masuk=tgl_masuk_invalid,
                expired=expired_invalid,
                kurs_beli="abc",
                jumlah_unit="abc",
                status=1,
                keterangan="1-?☉⛓∫ⰶ⦿ⶪ⪧⪪",
            )

            message_nama_barang = stock_page.get_message_nama_barang_error()
            message_group = stock_page.get_message_group_error()
            message_part_number = stock_page.get_message_part_number_error()
            message_ref_des = stock_page.get_message_ref_des_error()
            message_tgl_masuk = stock_page.get_message_tgl_masuk_error()
            message_expired_date = stock_page.get_message_expired_date_error()
            message_kurs_beli = stock_page.get_message_kurs_beli_error()
            message_jumlah_unit = stock_page.get_message_jumlah_unit_error()
            message_status = stock_page.get_message_status_error()
            message_keterangan = stock_page.get_message_keterangan_error()
            self.assertEqual(message_nama_barang, "")
            self.assertEqual(message_group, "")
            self.assertEqual(message_part_number, "")
            self.assertEqual(message_ref_des, "")
            self.assertEqual(message_tgl_masuk, "")
            self.assertEqual(
                message_expired_date, "The expired must be a date after or equal to tgl masuk.")
            self.assertEqual(message_kurs_beli,
                             "The kurs beli must be a number.")
            self.assertEqual(
                message_jumlah_unit, "The jumlah unit must be an integer.")
            self.assertEqual(message_status, "")
            self.assertEqual(message_keterangan, "")

        with self.subTest("2. empty inputs"):
            stock_page.add_stock(
                nama_barang="",
                group="",
                part_number="",
                ref_des="",
                tgl_masuk="",
                expired="",
                kurs_beli="",
                jumlah_unit="",
                status="",
                keterangan="",
            )

            message_nama_barang = stock_page.get_message_nama_barang_error()
            message_group = stock_page.get_message_group_error()
            message_part_number = stock_page.get_message_part_number_error()
            message_ref_des = stock_page.get_message_ref_des_error()
            message_tgl_masuk = stock_page.get_message_tgl_masuk_error()
            message_expired_date = stock_page.get_message_expired_date_error()
            message_kurs_beli = stock_page.get_message_kurs_beli_error()
            message_jumlah_unit = stock_page.get_message_jumlah_unit_error()
            message_status = stock_page.get_message_status_error()
            message_keterangan = stock_page.get_message_keterangan_error()
            self.assertEqual(
                message_nama_barang, "The nama barang field is required.")
            self.assertEqual(message_group, "The group field is required.")
            self.assertEqual(
                message_part_number, "The part number field is required.")
            self.assertEqual(message_ref_des, "The ref des field is required.")
            self.assertEqual(message_tgl_masuk, "")
            self.assertEqual(message_expired_date,
                             "The expired field is required.")
            self.assertEqual(message_kurs_beli, "")
            self.assertEqual(
                message_jumlah_unit, "The jumlah unit field is required.")
            self.assertEqual(message_status, "The status field is required.")
            self.assertEqual(message_keterangan,
                             "The keterangan field is required.")

        with self.subTest("3. correct inputs"):
            stock_page.add_stock(
                nama_barang="Test Name",
                group=1,
                part_number=util.random_part_number(),
                ref_des=util.random_ref_des(),
                tgl_masuk=tgl_masuk_valid,
                expired=expired_valid,
                kurs_beli=True,
                jumlah_unit=4,
                status=1,
                keterangan="Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.",
            )

            message = stock_page.get_message()
            self.assertEqual(message, "Data berhasil ditambah!")

        # outside skripsi
        # adds two more stock for test_add_site_stock
        with self.subTest(""):
            stock_page.add_stock(
                nama_barang=constant.STOCK_NAME_0,
                group=1,
                part_number=util.random_part_number(),
                ref_des=util.random_ref_des(),
                tgl_masuk=tgl_masuk_valid,
                expired=expired_valid,
                kurs_beli=True,
                jumlah_unit=0,
                status=1,
                keterangan="Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.",
            )

            message = stock_page.get_message()
            self.assertEqual(message, "Data berhasil ditambah!")

            stock_page.add_stock(
                nama_barang=constant.STOCK_NAME_3,
                group=1,
                part_number=util.random_part_number(),
                ref_des=util.random_ref_des(),
                tgl_masuk=tgl_masuk_valid,
                expired=expired_valid,
                kurs_beli=True,
                jumlah_unit=3,
                status=1,
                keterangan="Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.",
            )

            message = stock_page.get_message()
            self.assertEqual(message, "Data berhasil ditambah!")

    def test_edit_stock(self):
        stock_page = StockPage(self.driver)

        tgl_masuk_invalid, expired_invalid = util.random_invalid_tgl_masuk_and_expired()
        tgl_masuk_valid, expired_valid = util.random_valid_tgl_masuk_and_expired()

        # SOMETIMES ERROR
        with self.subTest("1. checking whether the data in the list view is the same as in the edit form"):
            stock_view = stock_page.edit_stock_list()
            stock_edit = stock_page.edit_stock_detail()

            self.assertEqual(stock_view["nama_barang"], stock_edit["nama_barang"])
            self.assertEqual(stock_view["group"], stock_edit["group"])
            self.assertEqual(stock_view["part_number"], stock_edit["part_number"])
            self.assertEqual(stock_view["ref_des"], stock_edit["ref_des"])
            self.assertEqual(stock_view["tgl_masuk"], stock_edit["tgl_masuk"])
            self.assertEqual(stock_view["expired"], stock_edit["expired"])
            self.assertEqual(stock_view["kurs_beli"], stock_edit["kurs_beli"])
            self.assertEqual(stock_view["jumlah_unit"], stock_edit["jumlah_unit"])
            self.assertEqual(stock_view["status"], stock_edit["status"])
            self.assertEqual(stock_view["keterangan"], stock_edit["keterangan"])

        with self.subTest("2. string inputs not regular characters, kurs beli not number, jumlah unit not integer, expired date before tgl masuk"):
            stock_page.edit_stock(
                nama_barang="1-?ⴙ⺻✷⤵≣⼺⥊ⅿ⇆⌂⹁⊹⣁ⰴ⻏⥺⪈",
                group="1-?☉⛓∫ⰶ⦿ⶪ⪧⪪",
                part_number="PL-3-?ⶪ⪧⪪⼺⥊ⅿ⇆",
                ref_des="⽗⾇q?ⶪ⪧⪪⼺",
                tgl_masuk=tgl_masuk_invalid,
                expired=expired_invalid,
                kurs_beli="abc",
                jumlah_unit="abc",
                status=1,
                keterangan="1-?☉⛓∫ⰶ⦿ⶪ⪧⪪",
            )

            message_nama_barang = stock_page.get_message_nama_barang_error()
            message_group = stock_page.get_message_group_error()
            message_part_number = stock_page.get_message_part_number_error()
            message_ref_des = stock_page.get_message_ref_des_error()
            message_tgl_masuk = stock_page.get_message_tgl_masuk_error()
            message_expired_date = stock_page.get_message_expired_date_error()
            message_kurs_beli = stock_page.get_message_kurs_beli_error()
            message_jumlah_unit = stock_page.get_message_jumlah_unit_error()
            message_status = stock_page.get_message_status_error()
            message_keterangan = stock_page.get_message_keterangan_error()
            self.assertEqual(message_nama_barang, "")
            self.assertEqual(message_group, "")
            self.assertEqual(message_part_number, "")
            self.assertEqual(message_ref_des, "")
            self.assertEqual(message_tgl_masuk, "")
            self.assertEqual(
                message_expired_date, "The expired must be a date after or equal to tgl masuk.")
            self.assertEqual(message_kurs_beli,
                             "The kurs beli must be a number.")
            self.assertEqual(
                message_jumlah_unit, "The jumlah unit must be an integer.")
            self.assertEqual(message_status, "")
            self.assertEqual(message_keterangan, "")

        with self.subTest("3. empty inputs"):
            stock_page.edit_stock(
                nama_barang="",
                group="",
                part_number="",
                ref_des="",
                tgl_masuk="",
                expired="",
                kurs_beli="",
                jumlah_unit="",
                status="",
                keterangan="",
            )

            message_nama_barang = stock_page.get_message_nama_barang_error()
            message_group = stock_page.get_message_group_error()
            message_part_number = stock_page.get_message_part_number_error()
            message_ref_des = stock_page.get_message_ref_des_error()
            message_tgl_masuk = stock_page.get_message_tgl_masuk_error()
            message_expired_date = stock_page.get_message_expired_date_error()
            message_kurs_beli = stock_page.get_message_kurs_beli_error()
            message_jumlah_unit = stock_page.get_message_jumlah_unit_error()
            message_status = stock_page.get_message_status_error()
            message_keterangan = stock_page.get_message_keterangan_error()
            self.assertEqual(
                message_nama_barang, "The nama barang field is required.")
            self.assertEqual(message_group, "")
            self.assertEqual(
                message_part_number, "The part number field is required.")
            self.assertEqual(message_ref_des, "The ref des field is required.")
            self.assertEqual(message_tgl_masuk, "")
            self.assertEqual(message_expired_date,
                             "The expired field is required.")
            self.assertEqual(message_kurs_beli, "")
            self.assertEqual(
                message_jumlah_unit, "The jumlah unit field is required.")
            self.assertEqual(message_status, "")
            self.assertEqual(message_keterangan,
                             "The keterangan field is required.")

        with self.subTest("4. correct inputs"):
            stock_page.edit_stock(
                nama_barang="Test Name",
                group=1,
                part_number=util.random_part_number(),
                ref_des=util.random_ref_des(),
                tgl_masuk=tgl_masuk_valid,
                expired=expired_valid,
                kurs_beli=True,
                jumlah_unit=4,
                status=1,
                keterangan="Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.",
            )

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

        table_empty = stock_page.get_data_table_empty()
        self.assertEqual(table_empty, "")


# dependent of add_site
class SiteRadarStockManagement(BaseTest):

    def test_view_site_stock(self):
        site_radar_stock_page = SiteRadarStockPage(self.driver)
        site_radar_stock_page.view_site_stock()

        table_empty = site_radar_stock_page.get_data_table_empty()
        self.assertTrue(table_empty == "" or table_empty == "No data available in table")

    def test_add_site_stock(self):
        site_radar_stock_page = SiteRadarStockPage(self.driver)

        with self.subTest("1. stock with unit 0 should not be added"):
            site_radar_stock_page.add_site_stock(constant.STOCK_NAME_0)

            stocks = site_radar_stock_page.get_all_stocks()
            self.assertNotIn(constant.STOCK_NAME_0, stocks)

        # dependent of add_stock
        with self.subTest("2. constant.STOCK_NAME_3 harusnya cuma bisa jadi input 3 kali"):
            site_radar_stock_page.add_site_stock(constant.STOCK_NAME_3)

            message = site_radar_stock_page.get_message_add_site_stock_error()
            self.assertEqual(message, "The stock has already been taken")

        with self.subTest("3. select on but not selecting"):
            site_radar_stock_page.add_site_stock("")

            message = site_radar_stock_page.get_message_add_site_stock_error()
            self.assertEqual(message, "This field is required")

        with self.subTest("4. not selecting stock"):
            site_radar_stock_page.add_site_stock("delete")

            message = site_radar_stock_page.get_message_add_site_stock_error()
            self.assertEqual(message, "This field is required")

        with self.subTest("5. valid inputs, random stocks"):
            site_radar_stock_page.add_site_stock("random")

            message = site_radar_stock_page.get_message()
            self.assertEqual(message, "Data Created!")

    def test_edit_site_stock(self):
        site_radar_stock_page = SiteRadarStockPage(self.driver)

        tgl_masuk_invalid, expired_invalid = util.random_invalid_tgl_masuk_and_expired()
        tgl_masuk_valid, expired_valid = util.random_valid_tgl_masuk_and_expired()

        with self.subTest():
            site_radar_stock_page.edit_site_stock(
                nama_barang="1-?ⴙ⺻✷⤵≣⼺⥊ⅿ⇆⌂⹁⊹⣁ⰴ⻏⥺⪈",
                group="1-?☉⛓∫ⰶ⦿ⶪ⪧⪪",
                part_number="PL-3-?ⶪ⪧⪪⼺⥊ⅿ⇆",
                ref_des="⽗⾇q?ⶪ⪧⪪⼺",
                tgl_masuk=tgl_masuk_invalid,
                expired=expired_invalid,
            )

            message_nama_barang = site_radar_stock_page.get_message_nama_barang_error()
            message_group = site_radar_stock_page.get_message_group_error()
            message_part_number = site_radar_stock_page.get_message_part_number_error()
            message_ref_des = site_radar_stock_page.get_message_ref_des_error()
            message_tgl_masuk = site_radar_stock_page.get_message_tgl_masuk_error()
            message_expired_date = site_radar_stock_page.get_message_expired_date_error()
            self.assertEqual(message_nama_barang, "")
            self.assertEqual(message_group, "")
            self.assertEqual(message_part_number, "")
            self.assertEqual(message_ref_des, "")
            self.assertEqual(message_tgl_masuk, "")
            self.assertEqual(
                message_expired_date, "The expired must be a date after tgl masuk.")

        with self.subTest():
            site_radar_stock_page.edit_site_stock(
                nama_barang="",
                group="",
                part_number="",
                ref_des="",
                tgl_masuk="",
                expired="",
            )

            message_nama_barang = site_radar_stock_page.get_message_nama_barang_error()
            message_group = site_radar_stock_page.get_message_group_error()
            message_part_number = site_radar_stock_page.get_message_part_number_error()
            message_ref_des = site_radar_stock_page.get_message_ref_des_error()
            message_tgl_masuk = site_radar_stock_page.get_message_tgl_masuk_error()
            message_expired_date = site_radar_stock_page.get_message_expired_date_error()
            self.assertEqual(message_nama_barang, "The nama barang field is required.")
            self.assertEqual(message_group, "")
            self.assertEqual(message_part_number, "The part number field is required.")
            self.assertEqual(message_ref_des, "The serial number field is required.")
            self.assertEqual(message_tgl_masuk, "The tgl masuk field is required.")
            self.assertEqual( message_expired_date, "The expired field is required.")

        with self.subTest():
            site_radar_stock_page.edit_site_stock(
                nama_barang="Test Edit Sited Stock Name",
                group=1,
                part_number=util.random_part_number(),
                ref_des=util.random_ref_des(),
                tgl_masuk=tgl_masuk_valid,
                expired=expired_valid,
            )

            message = site_radar_stock_page.get_message()
            self.assertEqual(message, "Data Edited!")

    def test_delete_site_stock(self):
        site_radar_stock_page = SiteRadarStockPage(self.driver)
        site_radar_stock_page.delete_site_stock()

        message = site_radar_stock_page.get_message()
        self.assertEqual(message, "Data Deleted!")


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
    # suite.addTest(ExpertManagement("test_add_expert"))
    # suite.addTest(ExpertManagement("test_edit_expert"))
    # suite.addTest(ExpertManagement("test_delete_expert"))

    # suite.addTest(SiteRadarManagement("test_view_site"))
    # suite.addTest(SiteRadarManagement("test_add_site"))
    # suite.addTest(SiteRadarManagement("test_delete_site"))

    # suite.addTest(DistributionManagement("test_view_distribution"))
    # suite.addTest(DistributionManagement("test_add_distribution"))
    # suite.addTest(DistributionManagement("test_edit_distribution"))
    # suite.addTest(DistributionManagement(
    #     "test_delete_distribution"))

    # suite.addTest(StockManagement("test_view_stock"))
    # suite.addTest(StockManagement("test_add_stock"))
    # suite.addTest(StockManagement("test_edit_stock"))
    # suite.addTest(StockManagement("test_delete_stock"))
    # suite.addTest(StockManagement("test_view_stock_recommendation"))

    suite.addTest(SiteRadarStockManagement(
        "test_view_site_stock"))
    suite.addTest(SiteRadarStockManagement("test_add_site_stock"))
    suite.addTest(SiteRadarStockManagement(
        "test_edit_site_stock"))
    suite.addTest(SiteRadarStockManagement(
        "test_delete_site_stock"))

    suite.addTest(AuthenticationLogout("test_logout"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
