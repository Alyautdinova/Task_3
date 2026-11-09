from pages.base_page import BasePage
from locators.account_profile_locators import AccountProfileLocators

class AccountProfilePage(BasePage):

    # метод нажатия на кнопку "История заказов"
    def click_history_of_orders_button(self):
        self.click(AccountProfileLocators.history_of_orders_button)

    # метод нажатия на кнопку "Выход"
    def click_logout_button(self):
        self.click(AccountProfileLocators.logout_button)

    