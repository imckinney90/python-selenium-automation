from pages.base_page import BasePage
from pages.header import Header
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.sign_in_page import SignInPage
from pages.search_results_page import SearchResultsPage
from pages.terms_conditions_page import TermsConditionsPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.sign_in_page =SignInPage(driver)
        self.terms_conditions_page = TermsConditionsPage(driver)