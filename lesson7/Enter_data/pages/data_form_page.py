from selenium.webdriver.common.by import By
from pages.config import *

class enter_data:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self._driver.maximize_window()
    
    # ввести данные из файла config в соответсвующие поля
    def send_info(self):
        (self._driver.find_element(By.CSS_SELECTOR, '[name="first-name"]')).send_keys(First_name)
        (self._driver.find_element(By.CSS_SELECTOR, '[name="last-name"]')).send_keys(Last_name)
        (self._driver.find_element(By.CSS_SELECTOR, '[name="address"]')).send_keys(Address)
        (self._driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]')).send_keys(Zip_code)
        (self._driver.find_element(By.CSS_SELECTOR, '[name="city"]')).send_keys(City)
        (self._driver.find_element(By.CSS_SELECTOR, '[name="country"]')).send_keys(Country)
        (self._driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]')).send_keys(Email)
        (self._driver.find_element(By.CSS_SELECTOR, '[name="phone"]')).send_keys(Phone_number)
        (self._driver.find_element(By.CSS_SELECTOR, '[name="job-position"]')).send_keys(Job_position)
        (self._driver.find_element(By.CSS_SELECTOR, '[name="company"]')).send_keys(Company)

    # нажать submit
    def submit(self):
        self._driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

class assert_fields:
    def __init__(self, browser):
        self._driver = browser

    def take_first_name_class(self):
        return (self._driver.find_element(By.CSS_SELECTOR, '[id="first-name"]')).get_attribute('class')

    def take_last_name_class(self):
        return (self._driver.find_element(By.CSS_SELECTOR, '[id="last-name"]')).get_attribute('class')

    def take_address_class(self):
        return (self._driver.find_element(By.CSS_SELECTOR, '[id="address"]')).get_attribute('class')

    def take_zip_code_class(self):
        return (self._driver.find_element(By.CSS_SELECTOR, '[id="zip-code"]')).get_attribute('class')

    def take_city_class(self):
        return (self._driver.find_element(By.CSS_SELECTOR, '[id="city"]')).get_attribute('class')

    def take_country_class(self):
        return (self._driver.find_element(By.CSS_SELECTOR, '[id="country"]')).get_attribute('class')

    def take_email_class(self):
        return (self._driver.find_element(By.CSS_SELECTOR, '[id="e-mail"]')).get_attribute('class')

    def take_phone_class(self):
        return (self._driver.find_element(By.CSS_SELECTOR, '[id="phone"]')).get_attribute('class')

    def take_job_position_class(self):
        return (self._driver.find_element(By.CSS_SELECTOR, '[id="job-position"]')).get_attribute('class')

    def take_company_class(self):
        return (self._driver.find_element(By.CSS_SELECTOR, '[id="company"]')).get_attribute('class')
