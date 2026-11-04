import allure

from pages.header_page import HeaderPage
from pages.constructor_page import ConstructorPage
from pages.modal_page import ModalPage
from data.urls import Urls

class TestBaseFunction:

    @allure.title('Переход по клику на «Конструктор»')
    @allure.description('Проверяем переход на главную страницу при нажатии на кнопку «Конструктор»')
    def test_go_to_constructor_page(self, driver):
        with allure.step('Нажатие на кнопку «Конструктор»'):
            headerPage = HeaderPage(driver)
            headerPage.open(Urls.BASE_URL)
            headerPage.click_constructor_button()

        with allure.step('Проверка, что оставились на главной странице'):
            assert headerPage.get_current_url() == Urls.BASE_URL

    @allure.title('Переход по клику на «Лента Заказов»')
    @allure.description('Проверяем переход на ленту заказов при нажатии на кнопку «Лента Заказов»')
    def test_go_to_feed_page(self, driver):
        with allure.step('Нажатие на кнопку «Лента Заказов»'):
            headerPage = HeaderPage(driver)
            headerPage.open(Urls.BASE_URL)
            headerPage.click_order_feed_button()

        with allure.step('Проверка редиректа на ленту заказов'):
            assert headerPage.get_current_url() == Urls.FEED_URL

    @allure.title('Клик на ингредиент')
    @allure.description('Проверяем открытие модалки ингредиента')
    def test_ingredient_modal_opened(self, driver):
        with allure.step('Открытие главной страницы'):
            headerPage = HeaderPage(driver)
            headerPage.open(Urls.BASE_URL)

        with allure.step('Нажатие на ингредиент'):
            constructorPage = ConstructorPage(driver)
            constructorPage.click_ingredient_button()

        with allure.step('Проверка открытии модалки'):
            modalPage = ModalPage(driver)
            assert modalPage.is_modal_opened()

    @allure.title('Клик на крестик в модалке ингредиента')
    @allure.description('Проверяем закрытие модалки ингредиента')
    def test_ingredient_modal_closed(self, driver):
        with allure.step('Открытие главной страницы'):
            headerPage = HeaderPage(driver)
            headerPage.open(Urls.BASE_URL)

        with allure.step('Нажатие на ингредиент'):
            constructorPage = ConstructorPage(driver)
            constructorPage.click_ingredient_button()

        with allure.step('Нажатие на крестик в модальном окне'):
            modalPage = ModalPage(driver)
            modalPage.click_close_modal_button

        with allure.step('Проверка, что модалка закрыта'):
            assert modalPage.is_modal_closed
    