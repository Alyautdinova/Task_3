from selenium.webdriver.common.by import By

class FeedLocators:
    first_order_card = [By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem')])[1]"]
    order_count_for_all_time = [By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class,'OrderFeed_number')]"]
    order_count_for_today = [By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class,'OrderFeed_number')]"]
    order_in_progress_list = [By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li"]
    order_ready_list = [By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]/li"]
