import pytest
import requests
import json

from selenium import webdriver
from faker import Faker
from data.urls import Urls
from pages.login_page import LoginPage

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    yield driver
    
    driver.quit()


# фикстура для создания пользователя
@pytest.fixture
def register_new_user():

    fake = Faker()

    # генерируем почту, пароль и имя пользователя
    name = fake.file_name()
    email = fake.email()
    password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    
    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
        }

    response = requests.post(Urls.REGISTER_URL, json=payload)

    token = response.json().get("accessToken")

    yield {"payload": payload, "token": token, "email": email, "password": password}
    
    # удаление юзера
    headers = {"Authorization": token}
    requests.delete(Urls.USER_URL, headers=headers)

# фикстура для входа через ui
@pytest.fixture
def logged_in_page(driver, register_new_user):
    loginPage = LoginPage(driver)
    loginPage.open(Urls.LOGIN_URL)

    loginPage.login(email=register_new_user["email"], password=register_new_user["password"])
    
    return loginPage

# фикстура для входа с ипользованием localStorage (написано с помощью ии)
@pytest.fixture
def logged_in_page2(driver, register_new_user):
    
    # 1. Открываем главную страницу
    driver.get(Urls.BASE_URL)
    
    # 2. Берем токены из API-фикстуры
    token = register_new_user["token"]
    refresh_token = register_new_user.get("refreshToken", token) 
    
    # 3. Формируем данные для localStorage
    auth_data = {
        "accessToken": token,
        "refreshToken": refresh_token
    }
    # Превращаем вложенный объект в строку, так как Redux-persist хранит все как строки
    auth_string = json.dumps(auth_data)
    
    # Записываем в localStorage.
    js_script = f"""
        localStorage.setItem('persist:root', JSON.stringify({{
            auth: {json.dumps(auth_string)}
        }}));
        
        // На всякий случай дублируем отдельными ключами (иногда React читает их напрямую)
        localStorage.setItem('accessToken', '{token}');
        localStorage.setItem('refreshToken', '{refresh_token}');
    """
    driver.execute_script(js_script)
    
    # 4. Обновляем страницу, чтобы React подхватил токены
    driver.refresh()
    
    return driver

# фикстура для получения валидных ID ингредиентов
@pytest.fixture
def get_valid_ingredients():
    response = requests.get(Urls.INGREDIENTS_URL)
    
    ingredients_data = response.json().get("data", [])
    return [ingredients_data[0]["_id"], ingredients_data[1]["_id"]]

# фикстура для создание заказа
@pytest.fixture
def created_order(register_new_user, get_valid_ingredients):
    token = register_new_user["token"]
    headers = {"Authorization": token}
    payload = {"ingredients": get_valid_ingredients}
    
    response = requests.post(Urls.ORDER_URL, json=payload, headers=headers)
    
    return {"order_number": response.json()["order"]["number"], "token": token}
