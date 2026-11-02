from selenium.webdriver.common.by import By

class ResetPasswordLocators:
    password_input = [By.XPATH, "//input[@type='password']"]
    hide_password_icon = [By.XPATH,  "//div[contains(@class, 'input__icon')]"]

    @staticmethod
    def active_password(password):
        return (By.XPATH,
                    f"//div[contains(@class, 'input_status_active')]/input[@value='{password}']")