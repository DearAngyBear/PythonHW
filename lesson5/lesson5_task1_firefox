from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

Click = driver.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]')
for x in range (1,6):
    Click.click()
    sleep(0.5)

delete_elements = driver.find_elements(By.CSS_SELECTOR, '[onclick="deleteElement()"]')

print(len(delete_elements))

sleep (2)
driver.close()