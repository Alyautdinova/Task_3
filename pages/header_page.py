from pages.base_page import BasePage
from locators.header_locators import HeaderLocators

class HeaderPage(BasePage):
    
    # метод нажатия на кнопку "Личный кабинет"
    def click_personal_account_button(self):
        self.click(HeaderLocators.personal_account_button)

    # метод нажатия на кнопку "Конструктор"
    def click_constructor_button(self):
        self.click(HeaderLocators.constructor_button)

    # метод нажатия на кнопку "Лента Заказов"
    def click_order_feed_button(self):
        self.click(HeaderLocators.order_feed_button)
    