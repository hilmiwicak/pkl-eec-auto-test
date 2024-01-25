from pages.base_page import BasePage


class DistributionPage(BasePage):

    def view_distribution(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/distribution']"
        ).click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn.btn-info").click()

    def add_distribution(self, name):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/distribution']"
        ).click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn.btn-info").click()
        self.driver.find_element(self.By.CSS_SELECTOR,
                                 "a.btn.btn-primary").click()

        distribution_sel_element = self.driver.find_element(
            self.By.ID, "site_id")
        distribution_sel = self.Select(distribution_sel_element)
        distribution_sel.select_by_index(1)

        distribution_expert_element = self.driver.find_element(
            self.By.ID, "expert_id")
        distribution_expert = self.Select(distribution_expert_element)
        distribution_expert.select_by_visible_text(name)

        super().click_submit_button_primary()
        self.driver.switch_to.alert.accept()

    def edit_distribution(self, name):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/distribution']"
        ).click()
        self.driver.find_elements(
            self.By.CSS_SELECTOR, "a.btn.btn-info")[1].click()
        self.driver.find_element(self.By.CSS_SELECTOR,
                                 "a.btn.btn-warning").click()

        distribution_expert_element = self.driver.find_element(
            self.By.ID, "expert_id")
        distribution_expert = self.Select(distribution_expert_element)
        distribution_expert.select_by_visible_text(name)

        super().click_submit_button_primary()
        self.driver.switch_to.alert.accept()

    def delete_distribution(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/distribution']"
        ).click()
        self.driver.find_elements(
            self.By.CSS_SELECTOR, "a.btn.btn-info")[1].click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "button.btn.btn-danger").click()
        self.driver.switch_to.alert.accept()
