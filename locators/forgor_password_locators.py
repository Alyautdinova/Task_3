from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    email_input = [By.XPATH, "//label[text()='Email']/following-sibling::input"]
    recovery_button = [By.XPATH, "//button[text()='Восстановить']"]