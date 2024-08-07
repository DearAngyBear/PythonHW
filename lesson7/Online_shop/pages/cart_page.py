from selenium.webdriver.common.by import By


class cart:
    def __init__(self, browser):
        self._driver = browser

    # перейти из корзины к оплате
    def Checkout(self):
        self._driver.find_element(By.ID, 'checkout').click()