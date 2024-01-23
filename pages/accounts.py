from pages.base_page import BasePage


class AccountPage(BasePage):

    def verify_account(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/userManagement']"
        ).click()
        self.driver.get(self.constant.BASE_URL + "/userManagement")
        self.time.sleep(500/1000)
        self.driver.find_element(
            self.By.CSS_SELECTOR, "button.btn-warning").click()
        self.time.sleep(500/1000)
        self.driver.switch_to.alert.accept()

        self.time.sleep(1)

    def delete_account(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/userManagement']"
        ).click()
        self.time.sleep(500/1000)
        self.driver.find_elements(
            self.By.CSS_SELECTOR, "button.btn-danger")[1].click()
        self.time.sleep(500/1000)
        self.driver.switch_to.alert.accept()
