from selenium.webdriver.common.by import By


class enter_information:
    def __init__(self, browser):
        self._driver = browser

    # заполнить личную информацию и подтвердить
    def set_info(self):
        self._driver.find_element(By.ID, "first-name").send_keys("Yuri")
        self._driver.find_element(By.ID, "last-name").send_keys("Drobot")
        self._driver.find_element(By.ID, "postal-code").send_keys("630009")
        self._driver.find_element(By.ID, "continue").click()