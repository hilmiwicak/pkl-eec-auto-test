from selenium.common.exceptions import NoSuchElementException
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
            self.By.ID, "input-current-password").send_keys(current_password)
        self.driver.find_element(self.By.ID, "input-password").send_keys(new_password)
        self.driver.find_element(
            self.By.ID, "input-password-confirmation").send_keys(confirmation_password)

        super().click_submit_button_primary()

    def get_message_current_password_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.ID, "name-error"
            )
            message_el.location_once_scrolled_into_view
            return message_el.text
        except self.NoSuchElementException:
            return ""


    def get_message_new_password_error(self):
        try:
            message_el = self.driver.find_element(
                self.By.ID, "password-error"
            )
            message_el.location_once_scrolled_into_view
            return message_el.text
        except self.NoSuchElementException:
            return ""
