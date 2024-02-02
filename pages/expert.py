from pages.base_page import BasePage


class ExpertPage(BasePage):

    def view_expert(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/expertManagement']"
        ).click()

    def add_expert(self, name, nip, expert_company=None):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/expertManagement']"
        ).click()
        self.time.sleep(1)
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn-primary").click()
        self.time.sleep(1)
        self.driver.find_element(
            self.By.ID, "name").send_keys(name)
        self.driver.find_element(
            self.By.ID, "nip").send_keys(nip)

        if expert_company is None:
            self.driver.find_element(self.By.ID, "eec_expert").click()
        else:
            self.driver.find_element(
                self.By.ID, "expert_company").send_keys(expert_company)

        super().click_submit_button_primary()
        self.driver.switch_to.alert.accept()

    def edit_expert(self, name, nip):
        # TODO: better one : let's say select the correct expert with the name
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/expertManagement']"
        ).click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn.btn-warning").click()
        name_input_element = self.driver.find_element(
            self.By.ID, "name")
        name_input_element.clear()
        name_input_element.send_keys(name)

        nip_input_element = self.driver.find_element(
            self.By.ID, "nip")
        nip_input_element.clear()
        nip_input_element.send_keys(nip)

        super().click_submit_button_primary()
        self.driver.switch_to.alert.accept()

    def delete_expert(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/expertManagement']"
        ).click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "button.btn.btn-danger").click()
        self.driver.switch_to.alert.accept()

    def get_message_name_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.XPATH,
                "//label[contains(@for, 'name')]/..//div[@class='invalid-feedback']"
            )
            return message_el.text
        except self.NoSuchElementException:
            return ""

    def get_message_nip_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.XPATH,
                "//label[contains(@for, 'nip')]/..//div[@class='invalid-feedback']"
            )
            return message_el.text
        except self.NoSuchElementException:
            return ""

    def get_message_company_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.XPATH,
                "//label[contains(@for, 'expert_company')]/..//div[@class='invalid-feedback']"
            )
            return message_el.text
        except self.NoSuchElementException:
            return ""
