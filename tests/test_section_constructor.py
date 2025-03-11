import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.data import get_exist_user_data
from src.locators import StellarBurgersLocators
from src.config import Config

class TestStellarBurgersConstructors:
    @pytest.mark.parametrize('text', ['Соусы', 'Начинки'])
    def test_transitions_to_sections(self, driver, text):
        driver.get(Config.URL)
        driver.find_element(By.XPATH, f".//span[text()='{text}']/parent::div").click()
        assert driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span").text == text