import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.testing2
@pytest.mark.parametrize('inp', [('15')])
def test_compare(inp):
    #Запуск браузера и переход на сайт
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    
    #Ввод значения 45
    driver.find_element(By.CSS_SELECTOR, '#delay').clear()
    driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(45)

    #Набор указанных данных на калькуляторе
    driver.find_element(By.XPATH,'//*[@id="calculator"]/div[2]/span[1]').click()
    driver.find_element(By.XPATH,'//*[@id="calculator"]/div[2]/span[4]').click()
    driver.find_element(By.XPATH,'//*[@id="calculator"]/div[2]/span[2]').click()
    driver.find_element(By.XPATH,'//*[@id="calculator"]/div[2]/span[15]').click()

    #Ожидание пока отработает веб-приложение
    WebDriverWait(driver, 46+1).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="calculator"]/div[1]/div'), '15')
    )

    #Запись значения в переменную
    result = driver.find_element(By.XPATH,'//*[@id="calculator"]/div[1]/div').text
    
    #Закрытие браузера
    driver.quit()

    #Сравнение результата
    assert result == inp


