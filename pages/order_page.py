import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from data.data import TestUrls
from data.generator import GeneratedData

class OrderPage(BasePage):
    @allure.step('Открыть страницу заказа')
    def open_page_order(self):
        self.start_page(TestUrls.OrderPageUrl)

    @allure.step('Заполнить контактную информацию для заказа')
    def enter_info(self, first_name=GeneratedData.generate_first_name(),
                   last_name=GeneratedData.generate_last_name(),
                   address=GeneratedData.generate_address(),
                   phone_number=GeneratedData.generate_phone_number()):
        self.add_value(OrderPageLocators.FIRST_NAME_INPUT, first_name)
        self.add_value(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.add_value(OrderPageLocators.ADDRESS_INPUT, address)
        self.add_value(OrderPageLocators.PHONE_NUMBER_INPUT, phone_number)

    @allure.step('Выбрать станцию метро')
    def choose_metro_station(self):
        self.click_element(OrderPageLocators.METRO_STATION_INPUT)
        self.click_element(OrderPageLocators.METRO_STATION_CLICK)

    @allure.step('Нажать на кнопку Далее')
    def click_next_button(self):
        self.find_element(OrderPageLocators.NEXT_BUTTON)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Выбрать дату "Когда привезти самокат?"')
    def choose_date(self):
        self.click_element(OrderPageLocators.DELIVERY_DATE_INPUT)
        self.click_element(OrderPageLocators.CHOICE_DATE_CALENDAR)

    @allure.step('Выбрать срок аренды')
    def choose_rent_period(self):
        self.click_element(OrderPageLocators.RENT_PERIOD)
        self.click_element(OrderPageLocators.CHOICE_RENT_PERIOD)

    @allure.step('Выбрать цвет самоката')
    def choose_color(self):
        self.click_element(OrderPageLocators.CHOICE_COLOR)

    @allure.step('Кликнуть на кнопку "Заказать"')
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click_element(OrderPageLocators.YES_ORDER_BUTTON_MODAL)

    @allure.step('Открыть страницу "Для кого самокат" и заполнить данными для заказа')
    def open_who_is_scooter_for_page(self):
        self.enter_info()
        self.choose_metro_station()
        self.click_next_button()

    @allure.step('Открыть страницу "Про аренду" и заполнить данными для заказа')
    def open_about_rent_page(self):
        self.choose_date()
        self.choose_rent_period()
        self.choose_color()
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.find_wait_location_element(OrderPageLocators.YES_ORDER_BUTTON_MODAL)
        self.confirm_order()
