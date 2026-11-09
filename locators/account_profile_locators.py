from selenium.webdriver.common.by import By

class AccountProfileLocators:
    history_of_orders_button = [By.XPATH, "//a[text()='История заказов']"]
    logout_button = [By.XPATH, "//button[text()='Выход']"]
