from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from time import sleep


EXPECTED_URL_PATTERN = "target.com/c/terms-conditions/-/N-4sr7l"
TNC_Link = (By.CSS_SELECTOR, '[aria-label="terms & conditions - opens in a new window"]')
TNC_TEXT = (By.CSS_SELECTOR,"[data-test='page-title']")

class TermsConditionsPage(BasePage):
    def store_original_window(self):
        self.original_window = self.driver.current_window_handle
        print(f"Current window handle: {self.original_window}")

    def click_tnc_link(self):
        TNC_Link = (By.CSS_SELECTOR, '[aria-label="terms & conditions - opens in a new window"]')
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TNC_Link),
            message="Terms & Conditions link not clickable."
        )
        self.driver.find_element(*TNC_Link).click()

    def switch_to_new_window(self):
        sleep(2)
        print('All windows', self.driver.window_handles)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def verify_terms_conditions_opened(self):
        expected_result = "Terms & Conditions"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TNC_TEXT),
            message="Terms & Conditions text not found on the page."
        )
        actual_result = self.driver.find_element(*TNC_TEXT).text
        assert expected_result == actual_result, f'Expected "{expected_result}" did not match "{actual_result}"'