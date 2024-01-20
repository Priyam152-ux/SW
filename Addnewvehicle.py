import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='/Users/priyammishra/PycharmProjects/SeleniumAutomation/chromedriver')

driver.get("https://prodadminsw.z29.web.core.windows.net/auth/login")

Sign_In = driver.find_element(By.XPATH, '/html/body/app-auth/div/div/div[2]/div[1]/app-login/div/form/div[5]/button')
Sign_In.click()

time.sleep(5)

vehicle_page = driver.get('https://prodadminsw.z29.web.core.windows.net/outlets/vehicles/add-vehicle?outletId'
                          '=fc0e5b34-81a9-4123 '
                          '-bfe2-394f9705a3e8')

driver.implicitly_wait(5)

select_partner = Select(driver.find_element(By.NAME, 'outlet'))
time.sleep(10)

select_partner_again = driver.find_element(By.NAME, 'outlet')
select_partner_again.click()
select_partner_again.click()
select_partner_again.click()
select_partner_again.click()

# select_partner.select_by_visible_text("Jettendra")
print(select_partner.select_by_index(1))

# time.sleep(5)
# select_partner.send_keys("Jettendra")
# select_partner.click()

# print(select_partner.first_selected_option.text)
