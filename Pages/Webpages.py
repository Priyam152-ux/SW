from selenium import webdriver
from selenium.webdriver.common.by import By

import Driver.Drivers

driver = Driver.Drivers.driver

selectcity = "html/body/app-root/app-header/p-sidebar/div/div[2]/div/div/div[2]/div[1]"


selectlocation = driver.find_element(By.XPATH,
                                     "/html/body/app-root/app-views/app-homepage/div/div[2]/form/div/span[1]/input")

selectpickup = driver.find_element(By.XPATH,
                                   '/html/body/app-root/app-views/app-homepage/div/div[2]/form/div/span[2]/input')

selectnext = driver.find_element(By.XPATH,
                                 '/html/body/p-dynamicdialog/div/div/div[2]/app-date-time-picker/div[2]/div[2]/div[4]/button')

selectdone = driver.find_element(By.XPATH,
                                 '/html/body/p-dynamicdialog/div/div/div[2]/app-date-time-picker/div[2]/div[2]/div[4]/button')

selectsearchmyride = driver.find_element(By.XPATH, '/html/body/app-root/app-views/app-homepage/div/div[3]/div/button')

selectclose = driver.find_element(By.XPATH,
                                  '/html/body/app-root/app-views/app-homepage/p-dialog/div/div/div[2]/div/button')

selectlocationagain = driver.find_element(By.XPATH,
                                          '/html/body/app-root/app-views/app-homepage/div/div[2]/form/div/span[1]/input')

selectoutlet = driver.find_element(By.XPATH,
                                   '/html/body/app-root/app-views/app-vendors/app-vendors-list/div/div[2]/div[2]/div/div[2]/button')

selectvehicle = driver.find_element(By.XPATH,
                                    '/html/body/app-root/app-views/app-vendors/app-vehicle-list/div[2]/div[2]/div[2]/div/div[2]/div[2]/button')

enterphone = driver.find_element(By.XPATH, '//*[@id="float-input"]')

getotpbutton = driver.find_element(By.XPATH,
                                   '/html/body/app-root/app-views/app-vendors/app-vehicle-list/p-dialog[2]/div/div/div[2]/div/div[2]/app-user-login/div/div/form[1]/div/span/span[2]')

enterotp = driver.find_element(By.XPATH,
                               '/html/body/app-root/app-views/app-vendors/app-vehicle-list/p-dialog[2]/div/div/div[2]/div/div[2]/app-user-login/div/div/form[2]/div[1]/input')

verifyotp = driver.find_element(By.XPATH,
                                '/html/body/app-root/app-views/app-vendors/app-vehicle-list/p-dialog[2]/div/div/div[2]/div/div[2]/app-user-login/div/div/form[2]/button')

selectvehicle = driver.find_element(By.XPATH,
                                    '/html/body/app-root/app-views/app-vendors/app-vehicle-list/div[2]/div[2]/div[2]/div/div[2]/div[2]/button')
