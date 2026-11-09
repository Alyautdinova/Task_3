from selenium.webdriver.common.by import By

class LoginLocator:
    forgot_password_button = [By.XPATH, "//a[text()='Восстановить пароль']"]
    email_input = [By.XPATH, "//label[text()='Email']/following-sibling::input"]
    password_input = [By.XPATH, "//input[@type='password']"]
    login_button = [By.XPATH, "//button[text()='Войти']"]
    