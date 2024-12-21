from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    CART_EMPTY_MSG = (By.CSS_SELECTOR,"[data-test='boxEmptyMsg']")

    def verify_cart_empty(self):
        expected_result = "Your cart is empty"
        actual_result = self.driver.find_element(*self.CART_EMPTY_MSG).text
        assert expected_result == actual_result, f'Expected {expected_result} did not match {actual_result}'

    def add_to_cart(self, product_name):
        self.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search"))).click()
        self.driver.find_element(By.CSS_SELECTOR, "#search").send_keys(product_name)
        self.driver.find_element(By.CSS_SELECTOR, ".sc-4596e520-3").click()

    def verify_product(self):
        expected_result = "Coca-Cola Soda - 10pk/7.5 fl oz Mini-Cans"
        actual_result = self.driver.find_element(By.CSS_SELECTOR, "[data-test='cartItem-title']").text
        assert expected_result == actual_result, f'Expected product {expected_result} did not match {actual_result}'