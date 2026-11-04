import pytest
import requests

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
    delete_response = requests.delete(Urls.USER_URL, headers=headers)
    assert delete_response.status_code == 202

# фикстура для входа через ui
@pytest.fixture
def logged_in_page(driver, register_new_user):
    loginPage = LoginPage(driver)
    loginPage.open(Urls.LOGIN_URL)

    loginPage.login(email=register_new_user["email"], password=register_new_user["password"])
    
    return loginPage
