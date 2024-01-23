from pages.base_page import BasePage


class LoginPage(BasePage):
    def login(self, email, password):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "input.form-control[type='email']").send_keys(email)
        self.driver.find_element(
            self.By.CSS_SELECTOR, "input.form-control[type='password']").send_keys(password)
        self.click_submit_button_primary()

    def logout(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link#navbarDropdownProfile").click()
        self.time.sleep(1)
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.dropdown-item[href='" + self.constant.BASE_URL + "/logout']").click()
