from pages.base_page import BasePage
from locators.feed_locators import FeedLocators

class FeedPage(BasePage):
    
    # метод нажатия на первую карточку заказа
    def click_first_order_card(self):
        self.click(FeedLocators.first_order_card)

    # метод возвращает количество заказов за все время
    def get_order_count_for_all_time(self):
        return int(self.get_text(FeedLocators.order_count_for_all_time))

    # метод возвращает количество заказов за сегодня   
    def get_order_count_for_today(self):
        return int(self.get_text(FeedLocators.order_count_for_today))

    # метод возвращает список номеров заказов в разделе "В работе"
    def get_in_progress_orders(self):
        elements = self.find_all(FeedLocators.order_in_progress_list)
    
        orders = []
        for el in elements:
            orders.append(el.text.lstrip('0'))
        
        return orders

    # метод возвращает список номеров заказов в разделе "Готовы"
    def get_ready_orders(self):
        elements = self.find_all(FeedLocators.order_ready_list)
    
        orders = []
        for el in elements:
            orders.append(el.text.lstrip('0'))
        
        return orders
    