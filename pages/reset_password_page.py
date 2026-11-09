from pages.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators

class ResetPasswordPage(BasePage):
    # метод заполнения поля "Пароль"
    def set_password(self, password):
        self.send_keys(ResetPasswordLocators.password_input, password)

    # метод нажатия на иконку скрыть/показать пароль
    def click_hide_password_icon(self):
        self.click(ResetPasswordLocators.hide_password_icon)

    # метод проверки, что поле "Пароль" активное
    def is_password_field_active(self, password):
        return self.find(ResetPasswordLocators.active_password(password))
    