from pages.base_page import BasePage
from locators.forgor_password_locators import ForgotPasswordLocators

class ForgotPasswordPage(BasePage):

    # метод заполнения поля "Email"
    def set_email(self, email):
        self.send_keys(ForgotPasswordLocators.email_input, email)

    # метод нажатия на кнопку "Восстановить"
    def click_recovery_button(self):
        self.click(ForgotPasswordLocators.recovery_button)

    # метод восстановления пароля
    def recovery(self, email):
        self.set_email(email)
        self.click_recovery_button()
    