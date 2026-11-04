from selenium.webdriver.common.by import By

class ConstructorLocators:
    ingredient_button = [By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]"]