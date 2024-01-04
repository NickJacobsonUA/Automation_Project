from conftest import driver
from pages.widgets_page import TestAccordianPage


class TestWidgets:

    class TestAccordianPage:
        # in this test I am going to compare the titles and the presense of the symbols in the content box
        def test_accordian(self,driver):
            accordian_page = TestAccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            #third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0
            assert second_title == 'Where does it come from?' and second_content > 0
            #assert third_title == 'Why do we use it?' and third_content > 0
            # unfortunately the third section would work because of the ads that doesn't let the driver click on it.


