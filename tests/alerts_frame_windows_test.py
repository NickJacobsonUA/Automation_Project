import time

from pages.alerts_frame_windows_page import BrowserWindowsPage
from conftest import driver


class Test_Alerts_Form_Windows:

    class Test_Browser_Windows:

        def test_new_tab(self,driver):
            browser_new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_new_tab_page.open()
            text_result = browser_new_tab_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', "A new tab has not been opened or incorrect tab has been opened"

        def test_new_window(self,driver):
            browser_new_window_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_new_window_page.open()
            text_result = browser_new_window_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', "A new window has not been opened or incorrect window has been opened"

