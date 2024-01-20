import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/Users/priyammishra/PycharmProjects/SeleniumAutomation/chromedriver')

driver.get('https://staging.scootywala.com/homev')

selectcity = driver.find_element(By.XPATH,
                                 '/html/body/app-root/app-header/p-sidebar/div/div[2]/div/div/div[2]/div[1]/div')
selectcity.click()

time.sleep(5)

# selectvehicle = driver.find_element(By.XPATH, '')

# scroll to end
scroll = driver.find_element(By.TAG_NAME, 'html')
scroll.send_keys(Keys.DOWN)
time.sleep(1)
scroll.send_keys(Keys.DOWN)
time.sleep(1)
