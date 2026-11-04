from pages.base_page import BasePage
from locators.modal_locators import ModalLocators

class ModalPage(BasePage):

    # метод проверки открытия модалки ингредиента
    def is_modal_opened(self):
        return self.find(ModalLocators.ingredient_deteils_title).is_displayed()

    # метод нажатия на крест
    def click_close_modal_button(self):
        self.click(ModalLocators.close_modal_button)

    # метод проверки исчезнвения модалки ингредиента
    def is_modal_closed(self):
        return self.wait_element_disappear(ModalLocators.ingredient_deteils_title)
    