from pages.base_page import BasePage


class MaintenancePage(BasePage):

    def view_pm(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/expertActivity']"
        ).click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn-info[href='" +
            self.constant.BASE_URL + "/pm']"
        ).click()

    def view_detail_pm(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/expertActivity']"
        ).click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn-info[href='" +
            self.constant.BASE_URL + "/pm']"
        ).click()
        self.driver.find_elements(
            self.By.CSS_SELECTOR, "a.btn.btn-info")[1].click()

    def view_cm(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/expertActivity']"
        ).click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn-info[href='" +
            self.constant.BASE_URL + "/cm']"
        ).click()
        
    def view_detail_cm(self):
        super().open_home()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.nav-link[href='" +
            self.constant.BASE_URL + "/expertActivity']"
        ).click()
        self.driver.find_element(
            self.By.CSS_SELECTOR, "a.btn-info[href='" +
            self.constant.BASE_URL + "/cm']"
        ).click()
        self.driver.find_elements(
            self.By.CSS_SELECTOR, "a.btn.btn-info")[1].click()
