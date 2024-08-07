import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from config import *

@pytest.mark.testing1
@pytest.mark.parametrize('selector',[
    ('zip-code'),
    ('first-name'),
    ('last-name'),
    ('address'),
    ('city'),
    ('country'),
    ('e-mail'),
    ('phone'),
    ('job-position'),
    ('company')
])

def test_fields(selector):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window

    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    (driver.find_element(By.CSS_SELECTOR, '[name="first-name"]')).send_keys(First_name)
    (driver.find_element(By.CSS_SELECTOR, '[name="last-name"]')).send_keys(Last_name)
    (driver.find_element(By.CSS_SELECTOR, '[name="address"]')).send_keys(Address)
    (driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]')).send_keys(Zip_code)
    (driver.find_element(By.CSS_SELECTOR, '[name="city"]')).send_keys(City)
    (driver.find_element(By.CSS_SELECTOR, '[name="country"]')).send_keys(Country)
    (driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]')).send_keys(Email)
    (driver.find_element(By.CSS_SELECTOR, '[name="phone"]')).send_keys(Phone_number)
    (driver.find_element(By.CSS_SELECTOR, '[name="job-position"]')).send_keys(Job_position)
    (driver.find_element(By.CSS_SELECTOR, '[name="company"]')).send_keys(Company)

    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    if selector == 'zip-code': 
        assert "danger" in driver.find_element(By.ID, selector).get_attribute('class')
    else:
        assert "succes" in driver.find_element(By.ID, selector).get_attribute('class')

    driver.quit()