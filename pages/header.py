from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage


class Header(BasePage):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGN_IN_LINK = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, '.sc-58ad44c0-3')




    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def click_cart(self):
        self.click(*self.CART_ICON)

    def sign_in_button(self):
        self.click(*self.SIGN_IN_BTN)

    def sign_in_link(self):
        self.click(*self.SIGN_IN_LINK)

