from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get('http://the-internet.herokuapp.com/inputs')

Space = driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div/input')

Space.send_keys('1000')
sleep (1) # задержка для наглядности работы скрипта
Space.clear()
sleep(1)# задержка для наглядности работы скрипта
Space.send_keys('999')

sleep(3)
driver.close()