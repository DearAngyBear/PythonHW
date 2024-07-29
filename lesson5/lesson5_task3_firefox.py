from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window()

driver.get(" http://uitestingplayground.com/classattr")

Click = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
Click.click()

sleep (2)
alert_obj = driver.switch_to.alert
alert_obj.accept()

sleep(2)
driver.close()