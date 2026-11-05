from selenium.webdriver.common.by import By

class ConstructorLocators:
    counter_ingredient_icon = [By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]//p"]
    basket_sector = [By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]"]
    order_button = [By.XPATH, "//button[text()='Оформить заказ']"]

    @staticmethod
    def ingredient_button_by_index(index):
        return (By.XPATH, f"(//a[contains(@class, 'BurgerIngredient_ingredient')])[{index}]")
    