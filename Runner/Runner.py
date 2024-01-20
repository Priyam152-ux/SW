import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# import Database.Database
import Driver.Drivers
import TestData.TestData
import Pages.Webpages

driver = Driver.Drivers.driver

driver.get(TestData.TestData.home)

driver.implicitly_wait(5)

selectcity = driver.find_element(By.XPATH, Pages.Webpages.selectcity)
selectcity.click()

driver.implicitly_wait(5)

selectlocation = Pages.Webpages.selectlocation
selectlocation.send_keys(TestData.TestData.Vehiclepickuplocation)
selectlocation.click()

selectpickup = Pages.Webpages.selectpickup
selectpickup.click()

selectnext = Pages.Webpages.selectnext
selectnext.click()

selectdone = Pages.Webpages.selectdone
selectdone.click()

selectsearchmyride = Pages.Webpages.selectsearchmyride
selectsearchmyride.click()

selectclose = Pages.Webpages.selectclose
selectclose.click()

selectlocationagain = Pages.Webpages.selectlocationagain
selectlocationagain.click()
selectlocationagain.send_keys(Keys.DOWN)
time.sleep(2)
selectlocationagain.send_keys(Keys.ENTER)
time.sleep(3)
selectsearchmyride.click()

selectoutlet = Pages.Webpages.selectoutlet
selectoutlet.click()

selectvehicle = Pages.Webpages.selectvehicle
selectvehicle.click()

enterphone = Pages.Webpages.enterphone
enterphone.send_keys(TestData.TestData.loginphone)

getotpbutton = Pages.Webpages.getotpbutton
getotpbutton.click()

Database.Database

print(Database.Database.otp[2])

enterotp = Pages.Webpages.enterotp
enterotp.send_keys(Database.Database.otp[2])

verifyotp = Pages.Webpages.verifyotp
verifyotp.click()

time.sleep(20)

selectvehicle = Pages.Webpages.selectvehicle
selectvehicle.click()

scroll = driver.find_element(By.TAG_NAME, 'html')
scroll.send_keys(Keys.DOWN)
time.sleep(1)
scroll.send_keys(Keys.DOWN)
time.sleep(1)
scroll.send_keys(Keys.DOWN)
time.sleep(1)
scroll.send_keys(Keys.DOWN)
time.sleep(1)
