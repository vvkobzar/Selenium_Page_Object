from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        self.driver.find_element(By.XPATH, "//a[@id='login_link']").click()

    def should_be_login_link(self):
        assert self.is_element_present(By.XPATH, "//a[@id='login_link']"), "Login link is not presented"
