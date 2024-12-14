from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.wait = WebDriverWait(driver, 10)

# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Table')

driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK'))).click()

# click search button
#driver.find_element(By.NAME, 'btnK').click()

# verify search results
assert 'Table'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()

# context.driver.wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//button[@data-test='@web/Search/SearchButton']"))).click()
# context.driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK'))).click()