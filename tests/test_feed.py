import allure
import requests

from pages.feed_page import FeedPage
from pages.modal_page import ModalPage
from pages.order_history_page import OrderHistoryPage
from data.urls import Urls

class TestFeed:
    @allure.title('Клик по заказу открывает модальное окно с деталями')
    @allure.description('Проверяем открытие модалки заказа')
    def test_click_order_opens_modal(self, logged_in_page2, created_order,  driver):
        with allure.step('Открытие главной Лента заказа'):
            feedPage = FeedPage(driver)
            feedPage.open(Urls.FEED_URL)

        with allure.step('Нажатие на первую карточку заказа'):
            feedPage.click_first_order_card()

        with allure.step('Проверка открытии модалки'):
            modalPage = ModalPage(driver)
            assert modalPage.is_feed_modal_opened()

    @allure.title('Заказы пользователя из истории отображаются в ленте заказов')
    @allure.title('Проверяем, что созданные заказы отображаются в истории и в ленте заказов')
    def test_user_orders_in_feed(self, logged_in_page2, created_order, driver):
        with allure.step('Открытие главной Лента заказа'):
            feedPage = FeedPage(driver)
            feedPage.open(Urls.FEED_URL)

        with allure.step('Проверка, созданные заказы отображаются в истории и в ленте заказов'):
            orderHistoryPage = OrderHistoryPage(driver)
            order_number_str = str(created_order["order_number"])
            assert order_number_str in orderHistoryPage.get_orders()
            assert order_number_str in feedPage.get_in_progress_orders() or order_number_str in feedPage.get_ready_orders() 

    @allure.title('Счетчик "Выполнено за всё время" увеличивается')
    @allure.description('Проверяем увеличение счетчика за все время при создании заказа')
    def test_total_counter_increases(self, logged_in_page2, register_new_user, get_valid_ingredients, driver):
        with allure.step('Открытие главной Лента заказа'):
            feedPage = FeedPage(driver)
            feedPage.open(Urls.FEED_URL)

        with allure.step('Берем изначальное значение заказов за все время'):
            initial_total = feedPage.get_order_count_for_all_time()

        with allure.step('Создаем заказ'):
            headers = {"Authorization": register_new_user["token"]}
            payload = {"ingredients": get_valid_ingredients}
            response = requests.post(Urls.ORDER_URL, json=payload, headers=headers)
            order_number = response.json()["order"]["number"]
            order_number_str = str(order_number)

        with allure.step('Проверяем количество заказов за все время'):
            assert order_number_str in feedPage.get_in_progress_orders() or order_number_str in feedPage.get_ready_orders()
            feedPage.open(Urls.FEED_URL)
            assert feedPage.get_order_count_for_all_time() > initial_total

    @allure.title('Счетчик "Выполнено сегодня" увеличивается')
    @allure.description('Проверяем увеличение счетчика за сегодня при создании заказа')
    def test_today_counter_increases(self, logged_in_page2, register_new_user, get_valid_ingredients, driver):
        with allure.step('Открытие главной Лента заказа'):
            feedPage = FeedPage(driver)
            feedPage.open(Urls.FEED_URL)
    
        with allure.step('Берем изначальное значение заказов за сегодня'):
            initial_today = feedPage.get_order_count_for_today()
    
        with allure.step('Создаем заказ'):
            headers = {"Authorization": register_new_user["token"]}
            payload = {"ingredients": get_valid_ingredients}
            response = requests.post(Urls.ORDER_URL, json=payload, headers=headers)
            order_number = response.json()["order"]["number"]
            order_number_str = str(order_number)
    
        with allure.step('Проверяем количество заказов за сегодня'):
            assert order_number_str in feedPage.get_in_progress_orders() or order_number_str in feedPage.get_ready_orders()
            feedPage.open(Urls.FEED_URL)
            assert feedPage.get_order_count_for_today() > initial_today

    @allure.title('Номер заказа появляется в разделе "В работе"')
    @allure.description('Проверяем, что номер заказа появляется в разделе "В работе"')
    def test_order_number_in_progress(self, logged_in_page, created_order, driver):
        with allure.step('Открытие главной Лента заказа'):
            feedPage = FeedPage(driver)
            feedPage.open(Urls.FEED_URL)

        with allure.step('Проверка, что заказ в разделе "В работе"'):
            assert str(created_order["order_number"]) in feedPage.get_in_progress_orders()
    