from pages.base_page import BasePage
from selenium.webdriver.common.by import By

LOGIN_FORM_TITLE = (By.CSS_SELECTOR, '#login')

class SignInPage(BasePage):
    def check_sign_in_form(self):
        expected_result = "Sign in with password"
        actual_result = self.driver.find_element(*LOGIN_FORM_TITLE).text
        assert expected_result == actual_result, f'Expected {expected_result} did not match {actual_result}'