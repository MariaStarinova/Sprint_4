#import allure
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPaigeLocators
from locators.order_page_locators import OrderPageLocators
from data.data import TestUrls

class MainPage(BasePage):

    #@allure.step('Главная страница')
    def main_url(self):
        self.start_page(TestUrls.MainPageUrl)

    #@allure.step('Принять cookie на главной странице')
    def get_cookie(self):
        self.find_element(BasePageLocators.ACCEPT_COOKIE_BUTTON)
        self.click_element(BasePageLocators.ACCEPT_COOKIE_BUTTON)

    #@allure.step('Блок cookies пропал')
    def cookie_not_displayed(self):
        return self.element_not_displayed(BasePageLocators.ACCEPT_COOKIE_BUTTON)

    #@allure.step('Кликнуть на логотип Яндекса в хедере страницы')
    def click_yandex_logo(self):
        self.wait_visibility_element(BasePageLocators.YANDEX_lOGO)
        self.click_element(BasePageLocators.YANDEX_lOGO)
        self.cross_new_window()
        self.wait_url_to_be(TestUrls.DzenMainUrl)
        assert self.driver.current_url == TestUrls.DzenMainUrl

       #@allure.step('Кликнуть на логотип "Самокат" в хедере страницы')
    def click_scooter_logo(self):
        self.wait_visibility_element(BasePageLocators.SCOOTER_LOGO)
        self.click_element(BasePageLocators.SCOOTER_LOGO)
        assert self.driver.current_url == TestUrls.MainPageUrl

   # @allure.step('Кликнуть по кнопке "Заказать" в хедере страницы')
    def click_header_order_button(self):
        self.click_element(BasePageLocators.HEADER_ORDER_BUTTON)
        self.find_wait_location_element(OrderPageLocators.HEADER_ORDER_PAGE)

    #@allure.step('Скролл до кнопки "Заказать" в body')
    def scroll_to_order_body_button(self):
        # self.get_cookie()
        self.scroll_to_element(MainPaigeLocators.BODY_ORDER_BUTTON)
        self.find_wait_location_element(MainPaigeLocators.BODY_ORDER_BUTTON)
        # self.wait_element_click(MainPaigeLocators.BODY_ORDER_BUTTON)
        # self.click_element(MainPaigeLocators.BODY_ORDER_BUTTON)

    #@allure.step('Кликнуть по кнопке "Заказать" в body')
    def click_to_order_body_button(self):
        self.scroll_to_order_body_button()
        self.click_element(MainPaigeLocators.BODY_ORDER_BUTTON)
        # # self.scroll_to_order_body_button()
        # # self.click_element(MainPaigeLocators.BODY_ORDER_BUTTON)
        # # self.find_wait_location_element(OrderPageLocators.HEADER_ORDER_PAGE)
        # self.get_cookie()
        # self.scroll_to_element(MainPaigeLocators.BODY_ORDER_BUTTON)
        # self.find_wait_location_element(MainPaigeLocators.BODY_ORDER_BUTTON)
        # # self.wait_element_click(MainPaigeLocators.BODY_ORDER_BUTTON)

    #@allure.step('Cкролл до блока вопросов')
    def scroll_question_path(self):
        self.scroll_to_element(MainPaigeLocators.QUESTION_PATH)

    #@allure.step('Кликнуть на вопрос в аккордеоне')
    def click_on_question(self, index):
        self.wait_visibility_element(MainPaigeLocators.QUESTION_PATH)
        questions = self.find_element(MainPaigeLocators.QUESTION_LOCATOR)
        questions[index].click()

    #@allure.step('Получить ответ на вопрос')
    def get_answers(self):
        self.wait_visibility_element(MainPaigeLocators.ANSWER_LOCATOR)
        return self.find_element(MainPaigeLocators.ANSWER_LOCATOR).text