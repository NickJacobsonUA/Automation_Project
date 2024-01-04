import time

from selenium.common import TimeoutException

from locators.widgets_page_locators import TestAccordianPageLocators
from pages.base_page import BasePage


class TestAccordianPage(BasePage):
    locators = TestAccordianPageLocators

    def check_accordian(self, accordian_num):

        # creating a dictionary to call the elements of the accordian
        accordian = {
            'first':
                {'title': self.locators.SECTION_FIRST,
                 'content': self.locators.SECTION_CONTENT_FIRST},
            'second':
                {'title': self.locators.SECTION_SECOND,
                 'content': self.locators.SECTION_CONTENT_SECOND},
            'third':
                {'title': self.locators.SECTION_THIRD,
                 'content': self.locators.SECTION_CONTENT_THIRD},
        }

        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        # there's a problem with the first section, cuz it's already opened when we load the page
        # so, we do not need to click the first section.
        # Going to use try-exception to solve the problem
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text  # taking the text
        except TimeoutException:  # in case TimeoutException happens we click it again and taking the text
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text  # taking the text
        return [section_title.text, len(section_content)]
