from pages.base_page import BasePage
from locators.order_history_locators import OrderHistoryLocators

class OrderHistoryPage(BasePage):

    # метод возвращает список номеров заказов
    def get_orders(self):
        elements = self.find_all(OrderHistoryLocators.order_history_list_number)
    
        orders = []
        for el in elements:
            orders.append(el.text.lstrip('#0'))
        
        return orders
    