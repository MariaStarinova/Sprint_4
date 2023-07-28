import allure
import pytest
from data.data import Answers
from pages.main_page import MainPage
from conftest import driver

@allure.feature('Раздел часто задаваемых вопросы')
class TestQuestions:
    @allure.title('Проверка списка часто задаваемых вопросов и ответов на главной странице')
    @allure.description('Раздел «Вопросы о важном» - при клике на вопрос открывается соответствующий ответ')
    @pytest.mark.parametrize("index", range(8))
    def test_click_on_questions(self, driver, index):
        main_page = MainPage(driver)
        main_page.main_url()
        main_page.get_cookie()
        main_page.scroll_question_path()
        main_page.click_on_question(index)
        answer = main_page.get_answers()
        assert answer == Answers.answers[index], 'Получен некорректный текст ответа'

