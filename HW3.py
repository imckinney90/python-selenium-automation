from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
#driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
#sleep(5)
#driver.find_element(By.CSS_SELECTOR, '.a-icon').click()
#driver.find_element(By.CSS_SELECTOR,"#ap_email").click()
#driver.find_element(By.CSS_SELECTOR,"#ap_password").click()
#driver.find_element(By.CSS_SELECTOR,"#ap_password_check").click()
#driver.find_element(By.CSS_SELECTOR,"#continue").click()
#driver.find_element(By.CSS_SELECTOR,"a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&amp;nodeId=508088']").click()

#sleep(5)



# 1 Optimal locators for Create Account on amazon.com
#Amazon Logo
# $$(".a-icon a-icon-logo")

# Your Name
# $$("#ap_customer_name")

# Mobile number or email
# $$("#ap_email")

# Password
# $$("#ap_password")

# Re-enter password
# $$("#ap_password_check")

# Continue
# $$("#continue")

# Conditions of Use
# $$("a[href*='ap_register_notification_condition_of_use']")

# Privacy Notice
# $$("a[href*='ap_register_notification_privacy_notice']")

# Sign In
# $$(".a-link-emphasis")

# 2. Create a test case using BDD that opens target.com, clicks on the cart icon and verifies that “Your cart is empty” message is shown:
# Open target.com
# Click on Cart icon
# Verify “Your cart is empty” message is shown

# Feature: Target.com Shopping Cart

#  Scenario:"Your cart is empty" message for carts without any items
#    Given I open the Target page
#    When I click on the cart icon
#    Then I should see the following message "Your cart is empty"


# 3. Create a test case using BDD to verify that a logged out user can navigate to Sign In:
# Open target.com
# Click Sign In
# From right side navigation menu, click Sign In
# Verify Sign In form opened

# Feature: User Sign In Navigation

#  Scenario:Logged out user can navigate to Sign In page
#    Given I open the Target page
#    When I click on Sign In
#    AND I click "Sign In" on the right side navigation menu
#    Then I should see the Sign In form page

