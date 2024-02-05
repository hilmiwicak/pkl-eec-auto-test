from pages.base_page import BasePage


class StockPage(BasePage):

    def view_stock(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/stocks']"
        ).click()

    def add_stock(self, stock_name, part_number, serial_number, tgl_masuk, expired_date, jumlah_unit, keterangan):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/stocks']"
        ).click()

        self.driver.find_element(
            self.By.CSS_SELECTOR,
            "a.btn-outline-primary[data-original-title='add item']"
        ).click()

        self.driver.find_element(
            self.By.ID, "nama_barang").send_keys(stock_name)

        self.driver.find_element(
            self.By.CSS_SELECTOR, "span.select2-selection__arrow").click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "li[aria-selected='false']").click()

        self.driver.find_element(
            self.By.ID, "part_number").send_keys(part_number)

        self.driver.find_element(
            self.By.ID, "ref_des").send_keys(serial_number)

        self.driver.find_element(self.By.ID, "tgl_masuk").send_keys(tgl_masuk)

        self.driver.find_element(self.By.ID, "expired").send_keys(expired_date)

        self.driver.find_element(self.By.ID, "button_kurs_beli").click()

        self.driver.find_element(
            self.By.ID, "jumlah_unit").send_keys(jumlah_unit)

        stock_status_element = self.driver.find_element(self.By.ID, "status")
        stock_status_element.location_once_scrolled_into_view
        stock_status_select = self.Select(stock_status_element)
        stock_status_select.select_by_value("Obsolete")

        self.driver.find_element(
            self.By.ID, "keterangan").send_keys(keterangan)

        super().click_submit_button_primary()

    def edit_stock(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/stocks']"
        ).click()

        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn.btn-warning").click()

        name_element = self.driver.find_element(self.By.ID, "nama_barang")
        name_element.clear()
        name_element.send_keys("Test Stock Edit")

        self.driver.find_element(
            self.By.CSS_SELECTOR, "span.select2-selection__arrow").click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "li[aria-selected='false']").click()

        part_number_element = self.driver.find_element(
            self.By.ID, "part_number")
        part_number_element.clear()
        part_number_element.send_keys(self.util.random_part_number())

        ref_des_element = self.driver.find_element(self.By.ID, "ref_des")
        ref_des_element.clear()
        ref_des_element.send_keys(self.util.random_serial_number())

        self.driver.find_element(self.By.ID, "tgl_masuk").send_keys("10262023")

        expired_element = self.driver.find_element(self.By.ID, "expired")
        expired_element.location_once_scrolled_into_view
        expired_element.send_keys("11262023")

        unit_element = self.driver.find_element(self.By.ID, "jumlah_unit")
        unit_element.clear()
        unit_element.send_keys("2")

        stock_status_element = self.driver.find_element(self.By.ID, "status")
        stock_status_element.location_once_scrolled_into_view
        stock_status_select = self.Select(stock_status_element)
        stock_status_select.select_by_value("Dummy")

        description_element = self.driver.find_element(
            self.By.ID, "keterangan")
        description_element.location_once_scrolled_into_view
        description_element.clear()
        description_element.send_keys("Keterangan Test Stock Edit")

        super().click_submit_button_primary()

    def delete_stock(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/stocks']"
        ).click()

        self.driver.find_element(
            self.By.CSS_SELECTOR, "button.btn.btn-danger").click()
        self.driver.switch_to.alert.accept()

    def view_stock_recommendation(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/stocks']"
        ).click()

        self.driver.find_element(
            self.By.CSS_SELECTOR, "a[data-original-title='recommendation item']").click()
