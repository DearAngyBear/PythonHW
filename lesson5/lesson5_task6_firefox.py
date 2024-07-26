from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get ('http://the-internet.herokuapp.com/login')

login = driver.find_element(By.XPATH,'//*[@id="username"]')
login.send_keys ('tomsmith')

password = driver.find_element(By.XPATH,'//*[@id="password"]')
password.send_keys ('SuperSecretPassword!')

button = driver.find_element (By.XPATH, '//*[@id="login"]/button')
button.click ()

sleep (3)
driver.close ()