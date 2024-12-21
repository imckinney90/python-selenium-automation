from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    SEARCH_RESULTS = (By.XPATH, "//div[@data-test='resultsHeading']")
    COCA_COLA = (By.CSS_SELECTOR, '[aria-label="Add Coca-Cola Soda - 10pk/7.5 fl oz Mini-Cans to cart"]')


    def verify_search_results(self, product):
        actual_result = self.find_element(*self.SEARCH_RESULTS).text
        assert product in actual_result, f'Expected text {product} not in actual {actual_result}'

    def add_cola_cart(self,):
        self.driver.wait.until(EC.presence_of_element_located(self.COCA_COLA)).click()
        self.driver.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test='orderPickupButton']"))).click()
        self.driver.get('https://www.target.com/cart')



