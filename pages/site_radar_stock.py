from pages.base_page import BasePage


class SiteRadarStockPage(BasePage):
    # this page is running only if there is site location constant.SITE_LOCATION
    # with site name "Test Radar Site"

    def view_site_stock(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/site']"
        ).click()
        card_element = self.driver.find_element(
            self.By.XPATH,
            """//strong[contains(text(), '{0}')]/ancestor::div[contains(@class, 'card card-stats')]""".format(
                self.constant.SITE_LOCATION)
        )
        card_element.location_once_scrolled_into_view
        card_element.find_element(
            self.By.CSS_SELECTOR, "a.btn-info").click()

    def add_site_stock(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/site']"
        ).click()

        card_element = self.driver.find_element(
            self.By.XPATH,
            """//strong[contains(text(), '{0}')]/ancestor::div[contains(@class, 'card card-stats')]""".format(
                self.constant.SITE_LOCATION)
        )
        card_element.location_once_scrolled_into_view
        card_element.find_element(
            self.By.CSS_SELECTOR, "a.btn-info").click()

        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn-outline-primary.text-right").click()

        for i in range(4):
            stock_sel_element = self.driver.find_element(
                self.By.CSS_SELECTOR, "select[name='stocks[" + str(i) + "][stock_id]']")
            stock_sel = self.Select(stock_sel_element)
            stock_sel.select_by_index(i+1)
            self.driver.find_element(
                self.By.CSS_SELECTOR, "button.btn-secondary").click()

        super().click_submit_button_primary()

    def edit_site_stock(self, name, part_number, serial_number, tgl_masuk, expired_date):
        self.driver.get(self.constant.BASE_URL + "/home")
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/site']"
        ).click()

        card_element = self.driver.find_element(
            self.By.XPATH,
            """//strong[contains(text(), '{0}')]/ancestor::div[contains(@class, 'card card-stats')]""".format(
                self.constant.SITE_LOCATION)
        )
        card_element.location_once_scrolled_into_view
        card_element.find_element(
            self.By.CSS_SELECTOR, "a.btn-info").click()

        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn-warning").click()

        name_input_element = self.driver.find_element(
            self.By.ID, "nama_barang")
        name_input_element.clear()
        name_input_element.send_keys(name)

        # random item group selection
        self.driver.find_element(
            self.By.CSS_SELECTOR, "span.select2-selection__arrow").click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "li[aria-selected='false']").click()

        # random part number input
        part_number_element = self.driver.find_element(
            self.By.ID, "part_number")
        part_number_element.clear()
        part_number_element.send_keys(part_number)

        # random serial number input
        self.driver.find_element(self.By.ID, "serial_number").send_keys(serial_number)

        # random date input
        self.driver.find_element(self.By.ID, "tgl_masuk").send_keys(tgl_masuk)

        # random date input
        self.driver.find_element(self.By.ID, "expired").send_keys(expired_date)

        super().click_submit_button_primary()

    def delete_site_stock(self):
        self.driver.get(self.constant.BASE_URL + "/home")
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/site']"
        ).click()

        card_element = self.driver.find_element(
            self.By.XPATH,
            """//strong[contains(text(), '{0}')]/ancestor::div[contains(@class, 'card card-stats')]""".format(
                self.constant.SITE_LOCATION)
        )
        card_element.location_once_scrolled_into_view
        card_element.find_element(
            self.By.CSS_SELECTOR, "a.btn-info").click()

        self.driver.find_element(
            self.By.CSS_SELECTOR, "button.btn-danger").click()

        self.driver.switch_to.alert.accept()
