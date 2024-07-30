import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import *


@pytest.mark.testing1
def test_shop():
    #Запуск браузера и переход на сайт
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')
    WebDriverWait(driver, 20)

    #Логин
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    #Добавление покупок в корзину
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    #Переход в корзину
    driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()

    #Нажатие Checkout
    driver.find_element(By.ID, 'checkout').click()

    #Ввод личных данных
    driver.find_element(By.ID, 'first-name').send_keys('Yuri')
    driver.find_element(By.ID, 'last-name').send_keys('Drobot')
    driver.find_element(By.ID, 'postal-code').send_keys('630009')
    driver.find_element(By.ID, 'continue').click()

    #Подводим итог
    Total = driver.find_element(By.CSS_SELECTOR, '[data-test="total-label"]').text
    driver.quit()

    #Сравниваем
    assert Right_total in Total

