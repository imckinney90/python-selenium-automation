from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

@when('Click on Cart Icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
sleep(10)

@then('Verify message of "Your cart is empty" is shown')
def verify_message(context):
    expected_result = "Your cart is empty"
    actual_result = context.driver.find_element(By.CSS_SELECTOR,"[data-test='boxEmptyMsg']").text
    assert expected_result == actual_result, f'Expected {expected_result} did not match {actual_result}'
