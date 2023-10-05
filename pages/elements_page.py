#Lesson 4
import time
# generated_person - библиотека с данными людей
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()
    # Создание функции для заполнения полей формы на странице https://demoqa.com/text-box
    # На странице 4 формы для заполнения
    # Симуляция печатания в поле функция send_keys()
    #next - функция для взятия данных для одной итерации для имени, фамилии и адреса


    def fill_all_fields(self, ):
        self.remove_footer()
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

# Теперь нужно написаь функции для вытягивания тескста после его заполнения из формы с помощью метода text()
    #функция split() убирает название переменных в принте, и оставляет только их значения.

    def check_field_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address