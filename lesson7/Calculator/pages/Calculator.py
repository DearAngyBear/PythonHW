from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    def __init__(self, browser):
        self._driver = browser

    # переходит на страницу с калькулятором
    def get(self):
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        self._driver.maximize_window()

    # вводит необходимую задержку
    def set_delay(self, time):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(time)

    # вывести искомый результат
    def take_result(self, delay, inp):
        WebDriverWait(self._driver, delay + 1).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, '//*[@id="calculator"]/div[1]/div'), inp
            )
        )
        return self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[1]/div'
        ).text

    # нажать нужную кнопку
    def clcik__1__(self):
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[9]'
        ).click()

    def clcik__2__(self):
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[10]'
        ).click()

    def clcik__3__(self):
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[11]'
        ).click()

    def clcik__4__(self):
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[5]'
        ).click()

    def clcik__5__(self):
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[6]'
        ).click()

    def clcik__6__(self):
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[7]'
        ).click()

    def clcik__7__(self):
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[1]'
        ).click()

    def clcik__8__(self):
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[2]'
        ).click()

    def clcik__9__(self):
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[3]'
        ).click()

    def clcik__0__(self):
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[3]'
        ).click()

    def click__multiply(self):
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[16]'
        ).click()

    def click__divide(self):
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[12]'
        ).click()

    def click__substraction(self):
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[8]'
        ).click()

    def click__summation(self):
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[4]'
        ).click()

    def click__result(self):
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[15]'
        ).click()

    def click__point(self):
        self._driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[14]'
        ).click()

    def click__clear(self):
        self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[1]/span').click()

    driver.quit()