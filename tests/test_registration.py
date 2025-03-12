from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.helpers import reg_new_user
from src.config import Config
from src.locators import StellarBurgersLocators

class TestStellarBurgersRegistration:

    def test_registration(self, driver):
        driver.get(f'{Config.URL}register')
        name_data, email_data, password_data = reg_new_user()
        driver.find_element(*StellarBurgersLocators.REG_NAME_FIELD).send_keys(name_data)
        driver.find_element(*StellarBurgersLocators.REG_EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*StellarBurgersLocators.REG_PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        assert driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).is_displayed()

    def test_error_registration(self, driver):
        driver.get(f'{Config.URL}register')
        name_data, email_data, password_data = reg_new_user()
        password_data = 'asdas'
        driver.find_element(*StellarBurgersLocators.REG_NAME_FIELD).send_keys(name_data)
        driver.find_element(*StellarBurgersLocators.REG_EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*StellarBurgersLocators.REG_PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        assert driver.find_element(*StellarBurgersLocators.INCORRECT_PASSWORD_LABEL).text == 'Некорректный пароль'