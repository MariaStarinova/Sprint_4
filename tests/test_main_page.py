#import allure
from data.data import TestUrls
from pages.main_page import MainPage
from conftest import driver

# @allure.feature('Действия на главной странице')
class TestMainPage:

    # @allure.title('Кнопка cookie "Да все привыкли"')
    # @allure.description('Нажать на кнопку "Да все привыкли", чтобы принять cookie')
    def test_accept_cookies(self, driver):
        main_page = MainPage(driver)
        main_page.main_url()
        main_page.get_cookie()
        assert main_page.cookie_not_displayed(), 'Блок cookies не пропал с экрана'

    # @allure.title('Проверка перехода со стартовой страницы по клику логотип "Яндекса"')
    # @allure.description('На странице нажать на логотип "Яндекса" в хедере, и происходит переход на страницу Яндекс.Дзен')
    def test_click_on_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.main_url()
        main_page.click_yandex_logo()
        assert driver.current_url == TestUrls.DzenMainUrl, 'URL-адрес не соответствует ожидаемому результату'

    # #  @allure.title('Проверка при клике на логотип "Самокат" остаемся на главной странице')
    # # @allure.description('На странице нажать на логотип "Самокат" в хедере на главной странице')
    def test_click_scooter_in_header(self, driver):
        main_page = MainPage(driver)
        main_page.main_url()
        main_page.click_scooter_logo()
        assert driver.current_url == TestUrls.MainPageUrl, 'URL-адрес не соответствует ожидаемому результату'

    # # @allure.title('Проверка перехода на страницу оформления заказа при клике на кнопку "Заказать" в хедере'
    # # @allure.description('Нажать на кнопку "Заказать" в хедере, и происходит переход на страницу заказа')
    def test_click_header_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.main_url()
        main_page.click_header_order_button()
        assert driver.current_url == TestUrls.OrderPageUrl, 'URL-адрес не соответствует ожидаемому результату'

    # @allure.title('Проверка перехода на страницу оформления заказа при клике на "Заказать" в body')
    # @allure.description('Нажать на кнопку "Заказать" в body, и происходит переход на страницу заказа')
    def test_click_body_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.main_url()
        main_page.get_cookie()
        main_page.click_to_order_body_button()
        assert driver.current_url == TestUrls.OrderPageUrl, 'URL-адрес не соответствует ожидаемому результату'
