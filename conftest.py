# Fixtures - функции, которые позволяют делать что то до или после теста
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# 1
@pytest.fixture(scope="function",)                   # function - для открытия браузера в set up и закрывался в teardown каждого теста. Независимость теста.
def driver():                           # открытие и закрытие функции. Для того что бы сделать функцию фикстурой прописывается декоратор сверху(смотреть выше)
                                            # driver = webdriver.Chrome #webdriver берётся из selenium. также нужно скачать драйвер менеджер - использовать спец. бтблиотеку webdriver manager
                                            # подключаем вэб драйвер мэнеджер через настройки и подключаем его через
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # импортируем бибилиотеку ChromeDriverManager() для открытия либо же запуска браузера
    driver.maximize_window()  # открытие браузера на весь экран
    yield driver
    driver.quit()  # закрытие браузера после завершения теста
    # После того как мы создали фикстуру мы переходим к созданию базовой страницы base_page.py
