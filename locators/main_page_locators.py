from selenium.webdriver.common.by import By

class MainPaigeLocators:
    BODY_ORDER_BUTTON = By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"
    QUESTION_LOCATOR = By.XPATH, "//div[contains(@class, 'accordion__item')]"
    ANSWER_LOCATOR = By.XPATH, "//div[contains(@class, 'accordion__panel') and not(@hidden)]"
    QUESTION_PATH = By.XPATH, ".//div[@class = 'Home_FourPart__1uthg']"
    DZEN_LOGO = By.XPATH, "//a[@aria-label='Логотип Дзен']"
