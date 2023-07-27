from selenium.webdriver.common.by import By

class BasePageLocators:
    ACCEPT_COOKIE_BUTTON = By.XPATH, " .//button[contains(@class, 'App_CookieButton')]"
    HEADER_ORDER_BUTTON = By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"
    YANDEX_lOGO = By.XPATH, ".//img[@alt='Yandex']"
    SCOOTER_LOGO = By.XPATH, ".//img[@alt='Scooter']"
