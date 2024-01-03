import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage
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

    class Test_Alerts_Page:
            def test_see_alert(self,driver):
                alert_page = AlertsPage(driver,'https://demoqa.com/alerts')
                alert_page.open()
                alert_text = alert_page.check_see_alert()
                assert alert_text == 'You clicked a button', 'The alert did not appear or the button was not clicked'

            def test_alert_appear_5_sec(self, driver):
                alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
                alert_page.open()
                alert_text = alert_page.check_alert_appear_5_sec()
                assert alert_text == 'This alert appeared after 5 seconds', 'The alert did not appear or the button was not clicked'

            def test_confirm_alert(self, driver):
                alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
                alert_page.open()
                alert_text = alert_page.check_confirm_alert()
                print(alert_text)
                assert alert_text == 'You selected Ok', 'The alert did not appear or the button was not clicked'

            def test_prompt_alert(self, driver):
                alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
                alert_page.open()
                text, alert_text = alert_page.check_prompt_alert()
                print(alert_text)
                print(text)
                assert alert_text == f'You entered {text}', 'The alert did not appear or the button was not clicked'

    class TestFramesPage:
        def test_frames(self,driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame_1 = frame_page.check_frame('frame1')
            result_frame_2 = frame_page.check_frame('frame2')
            assert result_frame_1 == ['This is a sample page', '500px', '350px'], 'The frame does not exist'
            assert result_frame_2 == ['This is a sample page', '100px', '100px'], 'The frame does not exist'

    class TestNestedFramesPage:
        def test_nested_frames(self,driver):
            nested_frame_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == 'Nested frame', 'Parent frame does not exist'
            assert child_text == 'Nested Iframe', 'Child frame does not exist'



