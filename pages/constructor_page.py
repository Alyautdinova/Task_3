from pages.base_page import BasePage
from locators.constuctor_locators import ConstructorLocators

class ConstructorPage(BasePage):

    # метод нажатия на ингредиент
    def click_ingredient_button(self):
        self.click(ConstructorLocators.ingredient_button)