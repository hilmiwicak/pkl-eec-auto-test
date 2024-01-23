from pages.base_page import BasePage


class ExpertPage(BasePage):

    def view_expert(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/expertManagement']"
        ).click()

    def add_not_eec_expert(self, name, nip, expert_company):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/expertManagement']"
        ).click()
        # add_element = self.driver.find_element(
        #     self.By.CSS_SELECTOR, "a.nav-link[href='" + self.constant.BASE_URL + "/expertManagement']")
        # self.driver.execute_script("arguments[0].click();", add_element)
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn-primary").click()
        self.driver.find_element(
            self.By.ID, "name").send_keys(name)
        self.driver.find_element(
            self.By.ID, "nip").send_keys(nip)
        self.driver.find_element(
            self.By.ID, "expert_company").send_keys(expert_company)
        super().click_submit_button_primary()
        self.driver.switch_to.alert.accept()

    def add_eec_expert(self, name, nip):
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
        self.driver.find_element(self.By.ID, "eec_expert").click()
        super().click_submit_button_primary()
        self.driver.switch_to.alert.accept()

    def edit_expert(self, name, nip):
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
