from selenium.webdriver.common.by import By

class OrderHistoryLocators:
    order_history_list_number = [By.XPATH, "//div[contains(@class, 'OrderHistory')]/p"]