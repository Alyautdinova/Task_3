from selenium.webdriver.common.by import By

class ModalLocators:
    ingredient_deteils_title = [By.XPATH, "//h2[text()='Детали ингредиента']"]
    close_modal_button = [By.XPATH, "//button[contains(@class,'Modal_modal__close')]"]
