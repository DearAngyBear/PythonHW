from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window

driver.get('http://uitestingplayground.com/textinput')

Field = driver.find_element (By.XPATH, '//*[@id="newButtonName"]')
Field.send_keys ('Sky Pro')

driver.find_element(By.XPATH,'//*[@id="updatingButton"]').click()

print(driver.find_element(By.XPATH,'//*[@id="updatingButton"]').text)
driver.quit()

