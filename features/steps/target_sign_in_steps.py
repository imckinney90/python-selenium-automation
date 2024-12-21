from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SIGN_IN_BTN = (By.CSS_SELECTOR, '.sc-58ad44c0-3')
SIGN_IN_LINK = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
LOGIN_FORM_TITLE = (By.CSS_SELECTOR, '#login')



@given('Open main page of target')
def open_main(context):
    context.app.main_page.open_main()


@when('Click Sign In button in the header')
def click_sign_in_btn(context):
    context.app.header.sign_in_button()

@when('Click "Sign In" link from the right-side navigation menu')
def click_sign_in_link(context):
    context.app.header.sign_in_link()


@then('See the Sign In form')
def check_sign_in_form(context):
    context.app.sign_in_page.check_sign_in_form()


