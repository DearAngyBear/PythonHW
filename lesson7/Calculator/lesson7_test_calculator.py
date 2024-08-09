import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.Calculator import *


def test_calculator():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    delay = 50  # выставить время ожидания - числовой параметр
    expected_result = "15"  # указать ожидаемый результат - строчный параметр

    calculator = Calculator(driver)
    calculator.get()
    calculator.set_delay(delay)
    calculator.clcik__7__()
    calculator.click__summation()
    calculator.clcik__8__()
    calculator.click__result()

    assert expected_result in calculator.take_result(delay, expected_result)

    driver.quit()