from appium import  webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UIAutomator2'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = 'Pixel'
desired_caps['appPackage'] = 'com.google.android.gm'
desired_caps['appActivity'] = 'com.google.android.gm.GmailActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# Handling Welcome screens
driver.find_element(AppiumBy.ID, "com.google.android.gm:id/welcome_tour_got_it").click()
time.sleep(3)
driver.find_element(AppiumBy.ID, "com.google.android.gm:id/setup_addresses_add_another").click()
time.sleep(5)
driver.find_element(AppiumBy.ID, "account_setup_item").click()

# Sign In
wait = WebDriverWait(driver, 30, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])
wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//*[@text='Sign in']"))
time.sleep(30)

driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").send_keys("deepthigumpula16@gmail.com")
driver.find_element(AppiumBy.XPATH, "//*[@text='NEXT']").click()
time.sleep(6)
driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").send_keys("Welcome@2626")
driver.find_element(AppiumBy.XPATH, "//*[@text='NEXT']").click()
time.sleep(15)
driver.find_element(AppiumBy.XPATH, "//*[@text='I agree']").click()
time.sleep(10)
driver.find_element(AppiumBy.ID, "com.google.android.gms:id/sud_items_switch").click()
time.sleep(5)
driver.find_element(AppiumBy.XPATH, "//*[@text='MORE']").click()
driver.find_element(AppiumBy.XPATH, "//*[@text='ACCEPT']").click()
time.sleep(3)
driver.find_element(AppiumBy.ID, "com.google.android.gm:id/action_done").click()
# Welcome to email
time.sleep(15)
driver.find_element(AppiumBy.XPATH, "//*[@text='Next']").click()
wait.until(lambda x: x.find_element(AppiumBy.ID, "com.google.android.gm:id/illustration_image_view"))
driver.find_element(AppiumBy.XPATH, "//*[@text='OK']").click()
# After logging into email
write_btn = driver.find_element(AppiumBy.ID,"com.google.android.gm:id/compose_button")
write_btn.click()
wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//*[@text='Smart Compose']"))

driver.find_element(AppiumBy.ID, "android:id/button1").click()
time.sleep(6)
if driver.find_element(AppiumBy.ID, "android:id/message"):
    driver.find_element(AppiumBy.ID, "android:id/button1").click()

wait.until(lambda x: x.find_element(AppiumBy.ID, "com.google.android.gm:id/from_account_name"))

driver.find_element(AppiumBy.ID, "com.google.android.gm:id/add_attachment").click()

wait.until(lambda x: x.find_element(AppiumBy.ID, "com.google.android.gm:id/title"))
driver.find_element(AppiumBy.ID, "com.google.android.gm:id/title").click()

wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.documentsui:id/apps_row"))
driver.find_element(AppiumBy.XPATH, "//*[@text='Photos']").click()
wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//*[@text='Select photos']"))
driver.find_element(AppiumBy.XPATH, "//*[@text='Pictures']").click()

wait = WebDriverWait(driver, 20)
print(len(driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'Photo taken')]")))
wait.until(lambda method: len(driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'Photo taken')]")) == 1)
driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'Photo taken')]").click()

time.sleep(4)
driver.find_element(AppiumBy.ID, "com.google.android.apps.photos:id/done_button").click()
time.sleep(10)
if driver.find_element(AppiumBy.ID, "android:id/message"):
    driver.find_element(AppiumBy.ID, "android:id/button1").click()

wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Preview of test.png']"))
driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Preview of test.png']").click()

driver.find_element(AppiumBy.ID, "com.google.android.gm:id/to").send_keys("deeptigumpula@gmail.com")

driver.find_element(AppiumBy.ID, "com.google.android.gm:id/subject").send_keys("Demo Email: Deepthi")

driver.find_element(AppiumBy.ID, "com.google.android.gm:id/send").click()

wait.until(lambda x: x.find_element(AppiumBy.ID, "com.google.android.gm:id/description_text"))
time.sleep(5)
