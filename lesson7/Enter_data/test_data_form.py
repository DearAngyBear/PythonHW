import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.data_form_page import *


def test_data_form():
    driver = webdriver.Chrome\
        (service=ChromeService(ChromeDriverManager().install()))

    first_action = enter_data(driver)
    first_action.send_info()
    first_action.submit()

    second_action = assert_fields(driver)
    
    assert "succes" in second_action.take_first_name_class()
    assert "succes" in second_action.take_last_name_class()
    assert "succes" in second_action.take_address_class()
    assert "succes" in second_action.take_email_class()
    assert "succes" in second_action.take_phone_class()
    assert "succes" in second_action.take_city_class()
    assert "succes" in second_action.take_country_class()
    assert "succes" in second_action.take_job_position_class()
    assert "succes" in second_action.take_company_class()
    assert "danger" in second_action.take_zip_code_class()
    
    driver.quit()