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


@when('Add to cart {product_name}')
def add_to_cart(context,product_name):
    context.driver.find_element(By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor12953464").click()
    sleep(10)


@when('Add {product_name} to the cart in the right-side menu')
def add_to_cart(context,product_name):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton']").click()
    sleep(10)
    context.driver.find_element(By.CSS_SELECTOR,"a[href='/cart']").click()
    sleep(10)

@then('Should see the product in my cart')
def verify_product(context):
    expected_result = "Coca-Cola Soda - 12pk/12 fl oz Cans"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cartItem-title']").text
    assert expected_result == actual_result, f'Expected product {expected_result} did not match {actual_result}'

