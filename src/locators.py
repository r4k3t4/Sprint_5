from selenium.webdriver.common.by import By


class StellarBurgersLocators:
    EMAIL_FIELD = By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default']/input"
    PASSWORD_FIELD = By.XPATH, "//div[@class='input pr-6 pl-6 input_type_password input_size_default']/input"
    LOGIN_BUTTON = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    ORDER_BUTTON = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
    ACCOUNT_BUTTON = By.XPATH, ".//a[@href='/account']/p"
    REG_BUTTON = By.XPATH, ".//a[@href='/register']"
    LOGOFF_BUTTON = By.XPATH, "//button[@class ='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"
    RECOVERY_PASSWORD_BUTTON = By.XPATH, ".//a[@href='/forgot-password']"
    AUTHENTICATION_BUTTON = By.XPATH, "//a[@class='Auth_link__1fOlj']"
    REG_NAME_FIELD = By.XPATH, "//label[text()='Имя']/../input"
    REG_EMAIL_FIELD = By.XPATH, "//label[text()='Email']/../input"
    REG_PASSWORD_FIELD = By.XPATH, "//input[@type='password']"
    INCORRECT_PASSWORD_LABEL = By.XPATH, "//p[@class='input__error text_type_main-default']"
    MAIN_PAGE = By.XPATH, "//main"
    ACTIVE_COLUMN_MENU = By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span"
    TITLE_TEXT = By.XPATH, "//h1"

