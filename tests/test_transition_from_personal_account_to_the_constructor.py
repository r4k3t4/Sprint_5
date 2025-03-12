import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.data import get_exist_user_data
from src.locators import StellarBurgersLocators
from src.config import Config

class TestStellarBurgersConstructor:
    @pytest.mark.parametrize("div", ["//a[@class = 'AppHeader_header__link__3D_hX' and @href='/']", "//div[contains(@class, 'AppHeader_header__logo__2D0X2')]"])
    def test_constructor(self, driver, div):
        driver.get(f"{Config.URL}login")
        driver.find_element(By.XPATH, div).click()
        assert driver.find_element(*StellarBurgersLocators.TITLE_TEXT).text == 'Соберите бургер'