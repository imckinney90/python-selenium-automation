from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open main paige of target')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Click Sign In button in the header')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '.sc-58ad44c0-3').click()
sleep(10)


@when('Click "Sign In" link from the right-side navigation menu')
def click_sign_in_link(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
sleep(10)


@then('See the Sign In form')
def check_sign_in_form(context):
    expected_result = "Sign in with password"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '#login').text
    assert expected_result == actual_result, f'Expected {expected_result} did not match {actual_result}'


# driver.find_element(By.CSS_SELECTOR, '.highlight')
# (By.CSS_SELECTOR,"['.sc-fe064f5c-0']").text
#'#my-element'