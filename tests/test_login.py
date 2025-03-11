import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.data import get_exist_user_data
from src.locators import StellarBurgersLocators
from src.config import Config

class TestStellarBurgersLogin:

    def test_login_to_account_button(self, driver):
        driver.get(Config.URL)
        email_data, password_data = get_exist_user_data()
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        assert driver.find_element(*StellarBurgersLocators.ORDER_BUTTON).text == "Оформить заказ"

    def test_personal_account(self, driver):
        driver.get(Config.URL)
        email_data, password_data = get_exist_user_data()
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        assert driver.find_element(*StellarBurgersLocators.ORDER_BUTTON).text == "Оформить заказ"

    def test_personal_account_through_registration(self, driver):
        driver.get(Config.URL)
        email_data, password_data = get_exist_user_data()
        driver.find_element(By.XPATH, ".//a[@href='/account']/p").click()
        driver.find_element(By.XPATH, ".//a[@href='/register']").click()
        driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj']").click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        assert driver.find_element(*StellarBurgersLocators.ORDER_BUTTON).text == "Оформить заказ"

    def test_personal_account_through_recover_password(self, driver):
        driver.get(Config.URL)
        email_data, password_data = get_exist_user_data()
        driver.find_element(By.XPATH, ".//a[@href='/account']/p").click()
        driver.find_element(By.XPATH, ".//a[@href='/forgot-password']").click()
        driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj']").click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        assert driver.find_element(*StellarBurgersLocators.ORDER_BUTTON).text == "Оформить заказ"