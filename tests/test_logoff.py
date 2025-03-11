import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.data import get_exist_user_data
from src.locators import StellarBurgersLocators
from src.config import Config

class TestStellarBurgersLogoff:

    def test_logoff_account_button(self, driver):
        driver.get(Config.URL)
        email_data, password_data = get_exist_user_data()
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default']/input").send_keys(email_data)
        driver.find_element(By.XPATH, "//div[@class='input pr-6 pl-6 input_type_password input_size_default']/input").send_keys(password_data)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//button[@class ='Account_button__14Yp3 text text_type_main-medium text_color_inactive']").click()
        driver.implicitly_wait(5)
        assert driver.find_element(By.XPATH, "//main").is_displayed()