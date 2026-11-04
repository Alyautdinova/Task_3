from pages.base_page import BasePage
from locators.header_locators import HeaderLocators

class HeaderPage(BasePage):
    
    # метод нажатия на кнопку "Личный кабинет"
    def click_personal_account_button(self):
        self.click(HeaderLocators.personal_account_button)
    