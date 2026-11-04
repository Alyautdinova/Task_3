import allure

from pages.header_page import HeaderPage
from pages.account_profile_page import AccountProfilePage
from data.urls import Urls

class TestPersonalAccount:

    @allure.title('Переход по клику на «Личный кабинет»')
    @allure.description('Проверяем переход на страницу аккаунта при нажатии на кнопку «Личный кабинет»')
    def test_go_to_personal_account(self, logged_in_page, driver):
        with allure.step('Нажатие на кнопку «Личный кабинет»'):
            headerPage = HeaderPage(driver)
            headerPage.click_personal_account_button()

        with allure.step('Проверка редиректа на страницу личного кабинета'):
            assert logged_in_page.is_current_url(Urls.PERSONAL_ACCOUNT_URL)

    @allure.title('Переход по клику на «История заказов»')
    @allure.description('Проверяем переход на страницу истории заказов при нажатии на кнопку «История заказов»')
    def test_go_to_order_history(self, logged_in_page, driver):
        with allure.step('Нажатие на кнопку «Личный кабинет»'):
            headerPage = HeaderPage(driver)
            headerPage.click_personal_account_button()

        with allure.step('Нажатие на кнопку «История заказов»'):
            accountProfilePage = AccountProfilePage(driver)
            accountProfilePage.click_history_of_orders_button()

        with allure.step('Проверка редиректа на страницу истории заказов'):
            assert accountProfilePage.is_current_url(Urls.ORDER_HISTORY_URL)

    @allure.title('Выход из аккаунта')
    @allure.description('Проверяем выход из личного кабинета')
    def test_logout(self, logged_in_page, driver):
        with allure.step('Нажатие на кнопку «Личный кабинет»'):
            headerPage = HeaderPage(driver)
            headerPage.click_personal_account_button()

        with allure.step('Выход из личного кабинета'):
            accountProfilePage = AccountProfilePage(driver)
            accountProfilePage.click_logout_button()

        with allure.step('Проверка редиректа на страницу логина'):
            assert accountProfilePage.is_current_url(Urls.LOGIN_URL)