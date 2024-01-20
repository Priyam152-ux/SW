import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Set up the webdriver and go to the IKEA website
driver = webdriver.Chrome(executable_path='/Users/priyammishra/PycharmProjects/SeleniumAutomation/chromedriver')
driver.get('https://www.amazon.in/')

# Wait for the DOM to load
wait = WebDriverWait(driver, 10)
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.range-revamp-header')))

# Get the initial state of the DOM
initial_dom = driver.page_source

# Trigger a DOM change (e.g. search for a product)
search_box = driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
search_box.send_keys('desk')
search_box.submit()

# Wait for the search results to load
time.sleep(5)
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.range-revamp-product-compact__info')))

# Get the new state of the DOM
new_dom = driver.page_source

# Compare the initial and new DOM states
if initial_dom != new_dom:
    print("DOM has changed")
else:
    print("DOM has not changed")

# Close the webdriver
driver.close()
