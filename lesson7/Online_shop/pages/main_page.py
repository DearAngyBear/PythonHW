from selenium.webdriver.common.by import By


class main_page:
    def __init__(self, browser):
        self._driver = browser

    # добавить нужные вещи в корзину
    def get_to_cart(self):
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # перейти в корзину
    def go_to_cart(self):
        self._driver.get("https://www.saucedemo.com/cart.html")