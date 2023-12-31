import time
import random

from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, \
    FramesPageLocators, NestedFramesPageLocators, ModalDialogsPageLocators
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

class FramesPage(BasePage):
    locators = FramesPageLocators
    #Checking that the iFrame exists and they contain the title "This is a sample page";
    #In order to check the difference between the 2 frames we are using the sizes of the frames;
    def check_frame(self,frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            # taking text from the frames by using self.driver
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content() #cleaning the content to be able to check the second frame
            return [text,width,height]

        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            # taking text from the frames by using self.driver
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text,width,height]

class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators
    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text,child_text

class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators
    def check_modal_dialogs(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        title_small = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
        body_small_text = self.element_is_visible(self.locators.BODY_SMALL_MODAL).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        title_large = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
        body_large_text = self.element_is_visible(self.locators.BODY_LARGE_MODAL).text
        return [title_small, len(body_small_text)], [title_large, len(body_large_text)]








