from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click Target Circle header button')
def click_target_circle(context):
    context.driver.find_element(By.CSS_SELECTOR, "#utilityNav-circle").click()
    sleep(10)






@then('See at least {expected_amount} benefit cells displayed on the page')
def step_verify_benefit_cells(context, expected_amount):
    expected_amount = int(expected_amount)
    benefit_cells = context.driver.find_elements(By.CSS_SELECTOR, '.cell-item-content')
    print('\nFind Benefit Cells:')
    print(benefit_cells)
    assert len(benefit_cells) >= (expected_amount), f"Expected at least {expected_amount} benefit cells, but found {len(benefit_cells)}"


