import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.authorization_form import authorize
from pages.main_page import main_page
from pages.cart_page import cart
from pages.enter_information import enter_information
from pages.confirm_page import confirm_page
from config import Right_total


def test_online_shop():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    shop = authorize(driver)
    shop.authorize()

    mainPage = main_page(driver)
    mainPage.get_to_cart()
    mainPage.go_to_cart()

    Cart = cart(driver)
    Cart.Checkout()

    info = enter_information(driver)
    info.set_info()

    confirm = confirm_page(driver)
    assert Right_total in confirm.Total_cost()

    driver.quit()