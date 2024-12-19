from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'search')
SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
RESULTS_HEADING = (By.XPATH, "//div[@data-test='resultsHeading']")


@given('Open target main page')
def open_main(context):
     context.driver.get('https://www.target.com/')



@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_INPUT).send_keys(product)
    context.driver.find_element(*SEARCH_BUTTON).click()


@then('Verify search results shown for {product}')
def verify_search_results(context, product):
    actual_result = context.driver.find_element(*RESULTS_HEADING).text
    assert product in actual_result, f'Expected text {product} not in actual {actual_result}'
