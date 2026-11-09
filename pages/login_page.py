from pages.base_page import BasePage
from locators.login_locators import LoginLocator

class LoginPage(BasePage):

    # метод нажатия на кнопку "Восстановить пароль"
    def click_forgot_password_button(self):
        self.click(LoginLocator.forgot_password_button)

    # метод заполнения поля "Email"
    def set_email(self, email):
        self.send_keys(LoginLocator.email_input, email)

    # метод заполнения поля "Пароль"
    def set_password(self, password):
        self.send_keys(LoginLocator.password_input, password)

    # метод нажатия на кнопку "Войти"
    def click_login_button(self):
        self.click(LoginLocator.login_button)

    # метод входа в личный кабинет
    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()
    
