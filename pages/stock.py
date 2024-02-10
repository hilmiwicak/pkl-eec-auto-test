from pages.base_page import BasePage


class StockPage(BasePage):

    def view_stock(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/stocks']"
        ).click()

    def add_stock_test(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/stocks']"
        ).click()

        self.driver.find_element(
            self.By.CSS_SELECTOR,
            "a.btn-outline-primary[data-original-title='add item']"
        ).click()

        super().click_submit_button_primary()

    def add_stock(self, nama_barang, group, part_number, ref_des, tgl_masuk, expired, kurs_beli, jumlah_unit, status, keterangan):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/stocks']"
        ).click()

        self.driver.find_element(
            self.By.CSS_SELECTOR,
            "a.btn-outline-primary[data-original-title='add item']"
        ).click()

        if nama_barang != "":
            nama_barang_el = self.driver.find_element(
                self.By.ID, "nama_barang")
            nama_barang_el.location_once_scrolled_into_view
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

        if part_number != "":
            part_number_el = self.driver.find_element(
                self.By.ID, "part_number")
            part_number_el.location_once_scrolled_into_view
            part_number_el.send_keys(part_number)

        if ref_des != "":
            ref_des_el = self.driver.find_element(
                self.By.ID, "ref_des")
            ref_des_el.location_once_scrolled_into_view
            ref_des_el.send_keys(ref_des)

        if tgl_masuk != "":
            tgl_masuk_el = self.driver.find_element(
                self.By.ID, "tgl_masuk")
            tgl_masuk_el.location_once_scrolled_into_view
            tgl_masuk_el.send_keys(tgl_masuk)

        if expired != "":
            expired_el = self.driver.find_element(
                self.By.ID, "expired")
            expired_el.location_once_scrolled_into_view
            expired_el.send_keys(expired)

        if (type(kurs_beli) == int) or (type(kurs_beli) == str):

            if kurs_beli != "":
                kurs_beli_el = self.driver.find_element(
                    self.By.ID, "kurs_beli")
                kurs_beli_el.location_once_scrolled_into_view
                kurs_beli_el.send_keys(kurs_beli)

        elif kurs_beli == True:
            button_kurs_beli_el = self.driver.find_element(
                self.By.ID, "button_kurs_beli")
            button_kurs_beli_el.location_once_scrolled_into_view
            button_kurs_beli_el.click()

        if (type(jumlah_unit) == int) or (type(kurs_beli) == str):

            if jumlah_unit != "":

                jumlah_unit_el = self.driver.find_element(
                    self.By.ID, "jumlah_unit")
                jumlah_unit_el.location_once_scrolled_into_view
                jumlah_unit_el.send_keys(jumlah_unit)

        stock_status_element = self.driver.find_element(self.By.ID, "status")
        stock_status_element.location_once_scrolled_into_view
        stock_status_select = self.Select(stock_status_element)

        if type(status) == int:
            stock_status_select.select_by_index(status)
        # random selection
        elif status != "":
            stock_status_select.select_by_value("Obsolete")

        if keterangan != "":
            keterangan_el = self.driver.find_element(
                self.By.ID, "keterangan")
            keterangan_el.location_once_scrolled_into_view
            keterangan_el.send_keys(keterangan)

        super().click_submit_button_primary()

    def edit_stock(self, nama_barang, group, part_number, ref_des, tgl_masuk, expired, kurs_beli, jumlah_unit, status, keterangan):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/stocks']"
        ).click()

        self.driver.find_element(
            self.By.CSS_SELECTOR,
            "a.btn-outline-primary[data-original-title='add item']"
        ).click()

        if nama_barang != "":
            nama_barang_el = self.driver.find_element(
                self.By.ID, "nama_barang")
            nama_barang_el.location_once_scrolled_into_view
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

        if part_number != "":
            part_number_el = self.driver.find_element(
                self.By.ID, "part_number")
            part_number_el.location_once_scrolled_into_view
            part_number_el.send_keys(part_number)

        if ref_des != "":
            ref_des_el = self.driver.find_element(
                self.By.ID, "ref_des")
            ref_des_el.location_once_scrolled_into_view
            ref_des_el.send_keys(ref_des)

        if tgl_masuk != "":
            tgl_masuk_el = self.driver.find_element(
                self.By.ID, "tgl_masuk")
            tgl_masuk_el.location_once_scrolled_into_view
            tgl_masuk_el.send_keys(tgl_masuk)

        if expired != "":
            expired_el = self.driver.find_element(
                self.By.ID, "expired")
            expired_el.location_once_scrolled_into_view
            expired_el.send_keys(expired)

        if (type(kurs_beli) == int) or (type(kurs_beli) == str):

            if kurs_beli != "":
                kurs_beli_el = self.driver.find_element(
                    self.By.ID, "kurs_beli")
                kurs_beli_el.location_once_scrolled_into_view
                kurs_beli_el.send_keys(kurs_beli)

        elif kurs_beli == True:
            button_kurs_beli_el = self.driver.find_element(
                self.By.ID, "button_kurs_beli")
            button_kurs_beli_el.location_once_scrolled_into_view
            button_kurs_beli_el.click()

        if (type(jumlah_unit) == int) or (type(kurs_beli) == str):

            if jumlah_unit != "":

                jumlah_unit_el = self.driver.find_element(
                    self.By.ID, "jumlah_unit")
                jumlah_unit_el.location_once_scrolled_into_view
                jumlah_unit_el.send_keys(jumlah_unit)

        stock_status_element = self.driver.find_element(self.By.ID, "status")
        stock_status_element.location_once_scrolled_into_view
        stock_status_select = self.Select(stock_status_element)

        if type(status) == int:
            stock_status_select.select_by_index(status)
        # random selection
        elif status != "":
            stock_status_select.select_by_value("Obsolete")

        if keterangan != "":
            keterangan_el = self.driver.find_element(
                self.By.ID, "keterangan")
            keterangan_el.location_once_scrolled_into_view
            keterangan_el.send_keys(keterangan)

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
                "//*[@id='ref_des']/../div[@class='invalid-feedback']"
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

    def get_message_kurs_beli_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.XPATH,
                "//*[@id='kurs_beli']/../div[@class='invalid-feedback']"
            )
            message_el.location_once_scrolled_into_view
            return message_el.text
        except self.NoSuchElementException:
            return ""

    def get_message_jumlah_unit_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.XPATH,
                "//*[@id='jumlah_unit']/../div[@class='invalid-feedback']"
            )
            message_el.location_once_scrolled_into_view
            return message_el.text
        except self.NoSuchElementException:
            return ""

    def get_message_status_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.XPATH,
                "//*[@id='status']/../div[@class='invalid-feedback']"
            )
            message_el.location_once_scrolled_into_view
            return message_el.text
        except self.NoSuchElementException:
            return ""

    def get_message_keterangan_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.XPATH,
                "//*[@id='keterangan']/../div[@class='invalid-feedback']"
            )
            message_el.location_once_scrolled_into_view
            return message_el.text
        except self.NoSuchElementException:
            return ""
