# Fixtures - функции, которые позволяют делать что то до или после теста
import pytest
import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



# 1
@pytest.fixture(scope="function",)
# function - для открытия браузера в set up и закрывался в teardown каждого теста. Независимость теста.
def driver():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))# импортируем бибилиотеку ChromeDriverManager() для открытия либо же запуска браузера
    driver.maximize_window()  # открытие браузера на весь экран
    yield driver
    driver.quit()  # закрытие браузера после завершения теста
    # После того как создали фикстуру переходим к созданию базовой страницы base_page.py
