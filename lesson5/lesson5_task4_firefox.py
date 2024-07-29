from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window()

driver.get(" http://the-internet.herokuapp.com/entry_ad")

sleep (2)
Click = driver.find_element(By.XPATH, '//*[@id="modal"]/div[2]/div[3]/p')
Click.click()

sleep (3)
driver.close()