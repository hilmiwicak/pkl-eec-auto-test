from pages.base_page import BasePage


class SiteRadarPage(BasePage):

    def view_site(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/site']"
        ).click()

    def add_site(self, radar_name, site_id, stock, image_path):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/site']"
        ).click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn-primary").click()

        self.driver.find_element(
            self.By.ID, "radar_name").send_keys(radar_name)
        self.driver.find_element(self.By.ID, "station_id").send_keys(site_id)

        if image_path != "":
            self.driver.find_element(self.By.ID, "image").send_keys(image_path)

        if type(stock) == int:
            for i in range(1, stock+1):
                stock_site_element = self.driver.find_element(
                    self.By.CSS_SELECTOR, "select[name='stocks[" + str(i-1) + "][stock_id]']")
                stock_site_select = self.Select(stock_site_element)
                stock_site_select.select_by_index(i)

                if i != stock:
                    self.driver.find_element(
                        self.By.CSS_SELECTOR, "button.btn-sm.btn-secondary").click()

        elif stock == "delete":
            self.driver.find_element(
                self.By.CSS_SELECTOR, "div#products_table div div a.d-inline.mt-4.ml-1").click()

        super().click_submit_button_primary()
        self.driver.switch_to.alert.accept()

    def delete_site(self):
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

        button_element = card_element.find_element(
            self.By.CSS_SELECTOR, "button.btn-danger")
        button_element.location_once_scrolled_into_view
        button_element.click()
        self.driver.switch_to.alert.accept()

    def get_message_radar_name_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.XPATH,
                "//input[contains(@name, 'radar_name')]/..//div[@class='invalid-feedback']"
            )
            return message_el.text
        except self.NoSuchElementException:
            return ""

    def get_message_station_id_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.XPATH,
                "//input[contains(@name, 'station_id')]/..//div[@class='invalid-feedback']"
            )
            return message_el.text
        except self.NoSuchElementException:
            return ""

    def get_message_stock_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.XPATH,
                "//select[contains(@class, 'site')]/../label[contains(@class, 'force-has-danger')]"
            )
            return message_el.text
        except self.NoSuchElementException:
            return ""

    def get_message_image_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.XPATH,
                "//input[@id='image']/..//div[@class='invalid-feedback']"
            )
            return message_el.text
        except self.NoSuchElementException:
            return ""
