from pages.base_page import BasePage


class ProfilePage(BasePage):

    def edit_password(self, current_password, new_password, confirmation_password):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link#navbarDropdownProfile").click()
        self.time.sleep(500/1000)
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.dropdown-item[href='" +
            self.constant.BASE_URL + "/profile']"
        ).click()

        self.time.sleep(500/1000)
        self.driver.find_element(
            "input-current-password").send_keys(current_password)
        self.driver.find_element("input-password").send_keys(new_password)
        self.driver.find_element(
            "input-password-confirmation").send_keys(confirmation_password)

        super().click_submit_button_primary()

    def get_message_current_password_error(self):
        return self.driver.find_element("name-error").text

    def get_message_new_password_error(self):
        return self.driver.find_element("password-error").text
