# Fixtures - функции, которые позволяют делать что то до или после теста
import pytest
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# 1
@pytest.fixture(scope="function",)
# function - для открытия браузера в set up и закрывался в teardown каждого теста. Независимость теста.
def driver():
    # открытие и закрытие функции. Для того что бы сделать функцию фикстурой прописывается декоратор сверху(смотреть выше)
    # driver = webdriver.Chrome #webdriver берётся из selenium. также нужно скачать драйвер менеджер - использовать спец. бтблиотеку webdriver manager
    # подключаем вэб драйвер мэнеджер через настройки и подключаем его через

    #выбор юзер по умолчанию при открытии браузера
    #options = webdriver.ChromeOptions()
    #options.add_argument("--profile-directory=Profile1")
    #options.add_argument("--user-data-dir=C:\\Users\\starl\\AppData\\Local\\Google\\Chrome\\User Data\\")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))# импортируем бибилиотеку ChromeDriverManager() для открытия либо же запуска браузера
    driver.maximize_window()  # открытие браузера на весь экран
    yield driver
    driver.quit()  # закрытие браузера после завершения теста
    # После того как создали фикстуру переходим к созданию базовой страницы base_page.py
