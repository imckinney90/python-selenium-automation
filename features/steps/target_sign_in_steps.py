from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SIGN_IN_BTN = (By.CSS_SELECTOR, '.sc-58ad44c0-3')
SIGN_IN_LINK = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
LOGIN_FORM_TITLE = (By.CSS_SELECTOR, '#login')
TNC_Link = (By.CSS_SELECTOR, '[aria-label="terms & conditions - opens in a new window"]')
TNC_TEXT = (By.CSS_SELECTOR,"[data-test='page-title']")

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

@given('Open Sign In page')
def open_main(context):
    context.app.main_page.open_main()
    context.app.header.sign_in_button()
    context.app.header.sign_in_link()

@when('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print(f"Current window handle: {context.original_window}")


@when('Click on Target terms and conditions link')
def click_tnc_link(context):
    TNC_Link = (By.CSS_SELECTOR, '[aria-label="terms & conditions - opens in a new window"]')
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(TNC_Link),
        message="Terms & Conditions link not clickable."
    )
    context.driver.find_element(*TNC_Link).click()

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    sleep(2)
    print('All windows',context.driver.window_handles)
    context.driver.switch_to.window(context.driver.window_handles[1])

@then('Verify Terms and Conditions page is opened')
def verify_terms_conditions_opened(context):
    expected_result = "Terms & Conditions"
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(TNC_TEXT),
        message="Terms & Conditions text not found on the page."
    )
    actual_result = context.driver.find_element(*TNC_TEXT).text
    assert expected_result == actual_result, f'Expected "{expected_result}" did not match "{actual_result}"'


@then('User can close new window and switch back to original')
def close_new_window_and_switch_back(context):
    if context.original_window not in context.driver.window_handles:
        raise Exception("Original window handle is no longer valid.")
    context.driver.close()
    print(f"Closed current window.")
    context.driver.switch_to.window(context.original_window)
    print(f"Switched back to original window: {context.original_window}")

