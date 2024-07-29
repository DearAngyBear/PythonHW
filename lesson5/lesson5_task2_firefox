from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://uitestingplayground.com/dynamicid")

Click = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')

Click.click()
driver.maximize_window()

sleep(3)
driver.close()