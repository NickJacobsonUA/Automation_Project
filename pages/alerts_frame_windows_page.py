import time
import random

from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators
from pages.base_page import BasePage



class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsPageLocators()
    # задача - при нажатии  кнопки new tab появлятся новая страница с текстом, нужно проверить что это новая таба
    # метод - работа с окнами "switch to"

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1]) # переключение внимания на окно с индексом 1, то есть новое окно
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1]) # переключение внимания на окно с индексом 1, то есть новое окно
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

class AlertsPage(BasePage):

    locators = AlertsPageLocators()

    # Кликаем на кнопки алертов и забираем значение из алертов через switch to и сравниваем

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click() #кликаем на кнопку
        #переключаемся на алерт и в берем текст из алерта с помощью alert.text
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    # алерт после 5 секунд
    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC).click()
        time.sleep(5)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    def check_prompt_alert(self):
        text = f"autotest{random.randint(0,999)}"
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_BOX_ALERT_RESULT).text
        return text, text_result

