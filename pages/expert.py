from pages.base_page import BasePage
from typing import List


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
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn-primary").click()
        self.driver.find_element("name").send_keys(name)
        self.driver.find_element("nip").send_keys(nip)

        if expert_company is None:
            self.driver.find_element("eec_expert").click()
        else:
            self.driver.find_element(
                "expert_company").send_keys(expert_company)

        super().click_submit_button_primary()
        self.driver.switch_to.alert.accept()

    def view_expert_detail(self) -> List[str]:
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/expertManagement']"
        ).click()
        tr_elements = self.driver.find_elements(self.By.CSS_SELECTOR, "tr")
        name = tr_elements[0].text
        nip = tr_elements[1].text
        expert_company = tr_elements[2].text
        return [name, nip, expert_company]

    def edit_expert_detail(self) -> List[str]:
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/expertManagement']"
        ).click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn.btn-warning").click()

        name = self.driver.find_element("name").get_attribute("value")
        nip = self.driver.find_element("nip").get_attribute("value")
        expert_company = self.driver.find_element("expert_company").get_attribute("value")

        return [name, nip, expert_company]

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
