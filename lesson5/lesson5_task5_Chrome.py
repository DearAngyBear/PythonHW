from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get('http://the-internet.herokuapp.com/inputs')

Space = driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div/input')

Space.send_keys('1000')
sleep (1) # задержка для наглядности работы скрипта
Space.clear()
sleep(1)# задержка для наглядности работы скрипта
Space.send_keys('999')

sleep (3)