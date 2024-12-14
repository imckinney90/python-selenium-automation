from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('Click Target Circle header button')
def click_target_circle(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#utilityNav-circle"))).click()


@then('See at least {expected_amount} benefit cells displayed on the page')
def step_verify_benefit_cells(context, expected_amount):
    expected_amount = int(expected_amount)
    benefit_cells = context.driver.find_elements(By.CSS_SELECTOR, '.cell-item-content')
    print('\nFind Benefit Cells:')
    print(benefit_cells)
    assert len(benefit_cells) >= (expected_amount), f"Expected at least {expected_amount} benefit cells, but found {len(benefit_cells)}"


