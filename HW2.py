from Tools.scripts.patchcheck import status
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


#1. Practice with locators.
#Amazon logo
#driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
#Amazon logo,search by XPATH,'a-icon a-icon-logo'

#Email field
#driver.find_element(By.ID,'ap_email')
#Email field, search by ID,'ap_email'

#Continue button
#driver.find_element(By.ID,'continue')
#Continue button,search by ID,'continue'

#Conditions of use link
#driver.find_element(By.XPATH,"//a[contains(@href,'gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use')]")
#Conditions,search by XPATH,'gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use'

#Privacy Notice link
#driver.find_element(By.XPATH,"//a[contains(@href,'customer/display.html/ref=ap_signin_notification_privacy_notice')]")
#Privacy Notice Link,search by XPATH,'customer/display.html/ref=ap_signin_notification_privacy_notice'

#Need help link
#driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']")
#Need help link, search by XPATH, 'Need help link'

#Forgot your password link
#driver.find_element(By.ID, 'auth-fpp-link-bottom')
#Forgot your password,search by ID,'auth-fpp-link-bottom'

#More ways to get support
#driver.find_element(By.ID, 'ap-other-signin-issues-link')
#More ways to get support,search by ID,'ap-other-signin-issues-link'

#Create your Amazon account button
#driver.find_element(By.ID,'createAccountSubmit')
#Create Amazon Account,search by ID,'createAccountSubmit'

#2. Create a test case for the SignIn page using python & selenium script.

# open the url
driver.get('https://www.target.com/ ')

# click sign in button  on homepage
driver.find_element(By.XPATH,"//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()

sleep (4)
# click sign in button on side navigation
driver.find_element(By.XPATH,"//button[@class='sc-ddc722c0-0 sc-f1230b39-0 jKTcnK doBYzz h-margin-t-x2 h-margin-b-default']").click()

sleep(8)


