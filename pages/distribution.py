from pages.base_page import BasePage


class DistributionPage(BasePage):

    def view_distribution_list_radar_name(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/distribution']"
        ).click()

        return self.driver.find_element(
            self.By.CSS_SELECTOR, "tr td:nth-child(2)").text

    def view_distribution_detail_radar_name(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/distribution']"
        ).click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn.btn-info").click()

        radar_name = self.driver.find_element(
            self.By.CSS_SELECTOR, "h4.card-title").text
        radar_name = radar_name.removeprefix("Expert Distribution of ")
        return radar_name

    def view_distribution_detail(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/distribution']"
        ).click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn.btn-info").click()

    def add_distribution_detail(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
                self.constant.BASE_URL + "/distribution']"
        ).click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn.btn-info").click()

        name_from_view = self.driver.find_elements(
            self.By.CSS_SELECTOR, "tr td:nth-child(2)")
        name_from_view = [name.text for name in name_from_view]

        self.driver.find_element(self.By.CSS_SELECTOR,
                                 "a.btn.btn-primary").click()

        select_expert_element = self.driver.find_element(
            self.By.ID, "expert_id")
        expert_element = self.Select(select_expert_element)
        name_list_from_select_detail = expert_element.options

        name_list_from_select_detail = [str(option.text) for option in name_list_from_select_detail]

        return [name_from_view, name_list_from_select_detail]

    def add_distribution(self, site_id, expert_id):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/distribution']"
        ).click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn.btn-info").click()
        self.driver.find_element(self.By.CSS_SELECTOR,
                                 "a.btn.btn-primary").click()

        if type(site_id) == int:
            site_id_select_element = self.driver.find_element(
                self.By.ID, "site_id")
            site_id_select = self.Select(site_id_select_element)
            site_id_select.select_by_index(site_id)

        expert_select_element = self.driver.find_element(
            self.By.ID, "expert_id")
        expert_select = self.Select(expert_select_element)

        # first if is outside skripsi
        if type(expert_id) == int:
            expert_select.select_by_index(expert_id)
        elif expert_id != "":
            expert_select.select_by_visible_text(expert_id)

        super().click_submit_button_primary()
        self.driver.switch_to.alert.accept()

    def edit_distribution_detail(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
                self.constant.BASE_URL + "/distribution']"
        ).click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn.btn-info").click()

        name_from_view = self.driver.find_elements(
            self.By.CSS_SELECTOR, "tr td:nth-child(2)")
        name_from_view = [name.text for name in name_from_view]

        self.driver.find_element(self.By.CSS_SELECTOR,
                                 "a.btn.btn-warning").click()

        select_expert_element = self.driver.find_element(
            self.By.ID, "expert_id")
        expert_element = self.Select(select_expert_element)
        name_list_from_select_detail = expert_element.options

        name_list_from_select_detail = [str(option.text) for option in name_list_from_select_detail]

        return [name_from_view, name_list_from_select_detail]

    def edit_distribution(self, expert_id):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/distribution']"
        ).click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn.btn-info").click()

        self.driver.find_element(self.By.CSS_SELECTOR,
                                 "a.btn.btn-warning").click()

        expert_select_element = self.driver.find_element(
            self.By.ID, "expert_id")
        expert_select = self.Select(expert_select_element)

        if expert_id != "":
            expert_select.select_by_index(expert_id)

        super().click_submit_button_primary()
        self.driver.switch_to.alert.accept()

    def delete_distribution(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/distribution']"
        ).click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn.btn-info").click()

        self.driver.find_element(
            self.By.CSS_SELECTOR, "button.btn.btn-danger").click()
        self.driver.switch_to.alert.accept()

    def get_message_site_id_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.XPATH,
                "//*[@id='site_id']/../div[@class='invalid-feedback']"
            )
            return message_el.text
        except self.NoSuchElementException:
            return ""

    def get_message_expert_id_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.XPATH,
                "//*[@id='expert_id']/../div[@class='invalid-feedback']"
            )
            return message_el.text
        except self.NoSuchElementException:
            return ""
