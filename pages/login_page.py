from pages.base_page import BasePage
from locators.login_locators import LoginLocator

class LoginPage(BasePage):

    # метод нажатия на кнопку "Восстановить пароль"
    def click_forgot_password_button(self):
        self.click(LoginLocator.forgot_password_button)
