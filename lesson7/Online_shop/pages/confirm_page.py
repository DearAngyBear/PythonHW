from selenium.webdriver.common.by import By

class confirm_page:
    def __init__(self, browser):
        self._driver = browser

    # вывести итоговое значение
    def Total_cost(self):
        return self._driver.find_element(By.CSS_SELECTOR, '[data-test="total-label"]').text
    