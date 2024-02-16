from pages.base_page import BasePage


class SiteRadarStockPage(BasePage):
    # this page is running only if there is site location constant.SITE_LOCATION
    # with site name "Test Radar Site" or constant.SITE_LOCATION

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

    def add_site_stock(self, stock):
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

        if stock == "delete":
            self.driver.find_element(
                self.By.CSS_SELECTOR, "div#products_table div div a.d-inline.mt-4.ml-1").click()
        elif stock == "random":
            for i in range(4):
                stock_sel_element = self.driver.find_element(
                    self.By.CSS_SELECTOR, "select[name='stocks[" + str(i) + "][stock_id]']")
                stock_sel = self.Select(stock_sel_element)
                stock_sel.select_by_index(i+1)
                self.driver.find_element(
                    self.By.CSS_SELECTOR, "button.btn-secondary").click()
        elif stock == self.constant.STOCK_NAME_3:
            for i in range(3):
                stock_sel_element = self.driver.find_element(
                    self.By.CSS_SELECTOR, "select[name='stocks[" + str(i) + "][stock_id]']")
                stock_sel = self.Select(stock_sel_element)
                stock_sel.select_by_visible_text(self.constant.STOCK_NAME_3)
                self.driver.find_element(
                    self.By.CSS_SELECTOR, "button.btn-secondary").click()

        if stock != self.constant.STOCK_NAME_0:
            super().click_submit_button_primary()


    def edit_site_stock(self, nama_barang, group, part_number, ref_des, tgl_masuk, expired):
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
            self.By.CSS_SELECTOR, "a.btn-warning").click()

        nama_barang_el = self.driver.find_element(
            self.By.ID, "nama_barang")
        nama_barang_el.location_once_scrolled_into_view
        nama_barang_el.clear()

        if nama_barang != "":
            nama_barang_el.send_keys(nama_barang)

        # the selection is usually random
        if type(group) == int:
            group_select_el = self.driver.find_element(
                self.By.ID, "group")
            group_select_el.location_once_scrolled_into_view
            group_select = self.Select(group_select_el)
            group_select.select_by_index(group)
        elif group != "":
            self.driver.find_element(
                self.By.CSS_SELECTOR, "span.select2-selection__arrow").click()
            self.driver.find_element(
                self.By.CSS_SELECTOR, "input.select2-search__field").send_keys(group)
            self.driver.find_element(
                self.By.CSS_SELECTOR, "input.select2-search__field").send_keys(self.Keys.ENTER)

        part_number_el = self.driver.find_element(
            self.By.ID, "part_number")
        part_number_el.location_once_scrolled_into_view
        part_number_el.clear()

        if part_number != "":
            part_number_el.send_keys(part_number)

        ref_des_el = self.driver.find_element(
            self.By.ID, "serial_number")
        ref_des_el.location_once_scrolled_into_view
        ref_des_el.clear()

        if ref_des != "":
            ref_des_el.send_keys(ref_des)

        tgl_masuk_el = self.driver.find_element(
            self.By.ID, "tgl_masuk")
        tgl_masuk_el.location_once_scrolled_into_view
        tgl_masuk_el.clear()

        if tgl_masuk != "":
            tgl_masuk_el.send_keys(tgl_masuk)

        expired_el = self.driver.find_element(
            self.By.ID, "expired")
        expired_el.location_once_scrolled_into_view
        expired_el.clear()

        if expired != "":
            expired_el.send_keys(expired)

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

    def get_all_stocks(self):
        try:
            stocks_el = self.driver.find_element(
                self.By.CSS_SELECTOR, ".form-control.site")
            stocks_sel = self.Select(stocks_el)
            return stocks_sel.options
        except self.NoSuchElementException:
            return []

    def get_message_add_site_stock_error(self):
        try:
            return self.driver.find_element(
                self.By.XPATH,
                "//select[contains(@class, 'site')]/../label[contains(@class, 'force-has-danger')]"
            ).text
        except self.NoSuchElementException:
            return ""

    def get_message_nama_barang_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.XPATH,
                "//*[@id='nama_barang']/../div[@class='invalid-feedback']"
            )
            message_el.location_once_scrolled_into_view
            return message_el.text
        except self.NoSuchElementException:
            return ""

    def get_message_group_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.XPATH,
                "//*[@id='group']/../div[@class='invalid-feedback']"
            )
            message_el.location_once_scrolled_into_view
            return message_el.text
        except self.NoSuchElementException:
            return ""

    def get_message_part_number_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.XPATH,
                "//*[@id='part_number']/../div[@class='invalid-feedback']"
            )
            message_el.location_once_scrolled_into_view
            return message_el.text
        except self.NoSuchElementException:
            return ""

    def get_message_ref_des_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.XPATH,
                "//*[@id='serial_number']/../div[@class='invalid-feedback']"
            )
            message_el.location_once_scrolled_into_view
            return message_el.text
        except self.NoSuchElementException:
            return ""

    def get_message_tgl_masuk_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.XPATH,
                "//*[@id='tgl_masuk']/../div[@class='invalid-feedback']"
            )
            message_el.location_once_scrolled_into_view
            return message_el.text
        except self.NoSuchElementException:
            return ""

    def get_message_expired_date_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.XPATH,
                "//*[@id='expired']/../div[@class='invalid-feedback']"
            )
            message_el.location_once_scrolled_into_view
            return message_el.text
        except self.NoSuchElementException:
            return ""
