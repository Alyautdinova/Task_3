from pages.base_page import BasePage
from locators.constuctor_locators import ConstructorLocators
from selenium.webdriver.common.action_chains import ActionChains

class ConstructorPage(BasePage):

    # метод нажатия на ингредиент
    def click_ingredient_button(self):
        self.click(ConstructorLocators.ingredient_button_by_index(1))

    # метод для драг-дропа ингредиента (написано ии)
    def drag_and_drop_ingredient(self, index):
        source = self.find(ConstructorLocators.ingredient_button_by_index(index))
        target = self.find(ConstructorLocators.basket_sector)

        # Эмуляция реального перетаскивания мышью
        ActionChains(self.driver) \
            .click_and_hold(source) \
            .move_to_element(target) \
            .release(target) \
            .perform()

    # метод получения количества ингредиентов    
    def get_ingredient_counter(self):
        return self.get_text(ConstructorLocators.counter_ingredient_icon)

    # метод нажатия на кнопку "Оформить заказ"
    def click_order_button(self):
        self.click(ConstructorLocators.order_button)

    # метод оформления заказа c булкой и соусом
    def order(self):
        self.drag_and_drop_ingredient(1)
        self.drag_and_drop_ingredient(3)
        self.click_order_button()
    