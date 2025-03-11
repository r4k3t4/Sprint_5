from selenium.webdriver.common.by import By


class StellarBurgersLocators:
    EMAIL_FIELD = By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default']/input"
    PASSWORD_FIELD = By.XPATH, "//div[@class='input pr-6 pl-6 input_type_password input_size_default']/input"
    LOGIN_BUTTON = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    ORDER_BUTTON = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
    ACCOUNT_BUTTON = By.XPATH, ".//a[@href='/account']/p"
