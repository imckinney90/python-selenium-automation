from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PRODUCT_URL = 'https://www.target.com/p/energen-tech-plus-2-running-shoes/-/A-92476719?preselect=92476740#lnk=sametab'


@given('Open product page')
def open_prod_page(context):
    context.driver.get(PRODUCT_URL)


@when('Product has multiple color options')
def find_color_options(context):

    context.color_options = context.driver.wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li[data-io-i] a[aria-label*='dusk purple'], li[data-io-i] a[aria-label*='white / white']"))
    )


    assert len(context.color_options) == 2, "Expected exactly 2 color options, found: " + str(len(context.color_options))
    print(f"Found {len(context.color_options)} color options.")


@then('Verify that color has been selected')
def verify_color_selected(context):
    for index, color in enumerate(context.color_options, start=1):

        context.driver.execute_script("arguments[0].scrollIntoView(true);", color)

        context.driver.wait.until(EC.element_to_be_clickable(color)).click()

        aria_label = color.get_attribute("aria-label")
        assert "selected" in aria_label.lower(), f"Color {index} is not selected. aria-label: {aria_label}"

        print(f"Color {index} selected successfully. Color: {aria_label}")








#context.driver.wait.until(EC.element_to_be_clickable(color)).click()