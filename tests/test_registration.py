from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.helpers import reg_new_user
from src.config import Config

class TestStellarBurgersRegistration:

    def test_registration(self, driver):
        driver.get(f'{Config.URL}register')
        name_data, email_data, password_data = reg_new_user()
        driver.find_element(By.XPATH, "//label[text()='Имя']/../input").send_keys(name_data)
        driver.find_element(By.XPATH, "//label[text()='Email']/../input").send_keys(email_data)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password_data)
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        assert driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").is_displayed()

    def test_error_registration(self, driver):
        driver.get(f'{Config.URL}register')
        name_data, email_data, password_data = reg_new_user()
        password_data = 'asdas'
        driver.find_element(By.XPATH, "//label[text()='Имя']/../input").send_keys(name_data)
        driver.find_element(By.XPATH, "//label[text()='Email']/../input").send_keys(email_data)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password_data)
        driver.find_element(By.XPATH,"//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        assert driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").text == 'Некорректный пароль'