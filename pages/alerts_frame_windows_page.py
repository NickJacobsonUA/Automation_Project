from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators
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
