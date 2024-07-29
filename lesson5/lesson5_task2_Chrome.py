from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("http://uitestingplayground.com/dynamicid")

Click = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
Click.click()

driver.maximize_window()

sleep(3)
driver.close()





