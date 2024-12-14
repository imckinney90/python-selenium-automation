from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Click on Cart Icon')
def click_cart_icon(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test='@web/CartLink']"))).click()


@then('Verify message of "Your cart is empty" is shown')
def verify_message(context):
    expected_result = "Your cart is empty"
    actual_result = context.driver.find_element(By.CSS_SELECTOR,"[data-test='boxEmptyMsg']").text
    assert expected_result == actual_result, f'Expected {expected_result} did not match {actual_result}'


@when('Add to cart {product_name}')
def add_to_cart(context,product_name):
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#search"))).click()
    context.driver.find_element(By.CSS_SELECTOR, "#search").send_keys(product_name)
    context.driver.find_element(By.CSS_SELECTOR, ".sc-4596e520-3").click()


@when('Add {product_name} to the cart in the right-side menu')
def add_to_cart(context,product_name):
   context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[aria-label="Add Coca-Cola Soda - 10pk/7.5 fl oz Mini-Cans to cart"]'))).click()
   context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test='orderPickupButton']"))).click()
   context.driver.get('https://www.target.com/cart')


@then('Should see the product in my cart')
def verify_product(context):
    expected_result = "Coca-Cola Soda - 10pk/7.5 fl oz Mini-Cans"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cartItem-title']").text
    assert expected_result == actual_result, f'Expected product {expected_result} did not match {actual_result}'