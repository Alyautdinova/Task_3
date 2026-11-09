import allure

from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from data.urls import Urls

class TestRecoveryPassword:
    
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('Проверяем, что при клике по кнопке «Восстановить пароль» открывается страница восстановления пароля')
    def test_go_to_forgot_password_page(self, driver):
        with allure.step('Открытие страницы логина'):
            loginPage = LoginPage(driver)
            loginPage.open(Urls.LOGIN_URL)

        with allure.step('Нажатие на кнопку «Восстановить пароль»'):
            loginPage.click_forgot_password_button()

        with allure.step('Проверка редиректа на страницу восстановления пароля'):
            assert loginPage.get_current_url() == Urls.FORGOT_PASSWORD_URL

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    @allure.description('Проверяем, что при клике по кнопке «Восстановить» открывается страница сброса пароля')
    def test_submit_email_for_recovery(self, driver):
        with allure.step('Открытие страницы восстановления пароля'):
            forgotPasswordPage = ForgotPasswordPage(driver)
            forgotPasswordPage.open(Urls.FORGOT_PASSWORD_URL)
        
        with allure.step('Ввод почты и нажатие на кнопку «Восстановить»'):
            forgotPasswordPage.recovery("test@example.com")
        
        with allure.step('Проверка редиректа на страницу сброса пароля'):
            assert forgotPasswordPage.is_current_url(Urls.RESET_PASSWORD_URL)

    @allure.title('Клик по иконке показать/скрыть пароль подсвечивает поле «Пароль»')
    @allure.description('Проверяем, что при клике на иконку глаза поле «Пароль» подсвечивается')
    def test_password_visibility_toggle_highlights_field(self, driver):
        new_password = "new_password_123"

        with allure.step('Открытие страницы восстановления пароля'):
            forgotPasswordPage = ForgotPasswordPage(driver)
            forgotPasswordPage.open(Urls.FORGOT_PASSWORD_URL)
            forgotPasswordPage.recovery("test@example.com")

        with allure.step('Ввод пароля и нажатие на иноку глаза'):
            resetPasswordPage = ResetPasswordPage(driver)
            resetPasswordPage.set_password(new_password)
            resetPasswordPage.click_hide_password_icon()

        with allure.step('Проверка, что поле «Пароль» подсвечивается'):
            assert resetPasswordPage.is_password_field_active(new_password)
    