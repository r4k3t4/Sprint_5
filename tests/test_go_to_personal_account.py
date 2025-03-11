import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.data import get_exist_user_data
from src.locators import StellarBurgersLocators
from src.config import Config

class TestStellarBurgersPersonalAccount:

    def test_transition_from_personal_account(self, driver):
        driver.get(Config.URL)
        email_data, password_data = get_exist_user_data()
        driver.find_element(*StellarBurgersLocators.ORDER_BUTTON).click()
        assert driver.current_url == Config.PROFILE_URL or driver.current_url == Config.LOGIN_URL


