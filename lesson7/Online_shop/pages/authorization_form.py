from selenium.webdriver.common.by import By

class authorize:
    
    def __init__ (self, browser):
        self._driver = browser
        self._driver.get('https://www.saucedemo.com/')
        self._driver.maximize_window()
    
    # авторизоваться
    def authorize(self):
        self._driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self._driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self._driver.find_element(By.ID, 'login-button').click()
   
    
