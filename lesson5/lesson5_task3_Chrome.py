from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get(" http://uitestingplayground.com/classattr")

Click = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
Click.click()

sleep (2)
alert_obj = driver.switch_to.alert
alert_obj.accept()

sleep (2)
driver.close()