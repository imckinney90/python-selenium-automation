from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CART_ICON = (By.CSS_SELECTOR,"[data-test='@web/CartLink']")
COCA_COLA = (By.CSS_SELECTOR,'[aria-label="Add Coca-Cola Soda - 10pk/7.5 fl oz Mini-Cans to cart"]')
ADD_TO_CART = (By.CSS_SELECTOR,"[data-test='orderPickupButton']")



@given('Open main page')
def open_main(context):
    context.app.main_page.open_main()


@when('Click on Cart Icon')
def click_cart_icon(context):
   context.app.header.click_cart()

@then('Verify message of "Your cart is empty" is shown')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()


@when('Add to cart {product_name}')
def add_to_cart(context,product_name):
    context.app.cart_page.add_to_cart(product_name)


@when('Add {product_name} to the cart in the right-side menu')
def add_to_cart(context,product_name):
   context.app.search_results_page.add_cola_cart()


@then('Should see the product in my cart')
def verify_product(context):
    context.app.cart_page.verify_product()