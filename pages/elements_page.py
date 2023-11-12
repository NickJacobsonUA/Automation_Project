#Lesson 4
import random
import time
# generated_person - библиотека с данными людей
from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()
    # Создание функции для заполнения полей формы на странице https://demoqa.com/text-box
    # На странице 4 формы для заполнения
    # Симуляция печатания в поле функция send_keys()
    #next - функция для взятия данных для одной итерации для имени, фамилии и адреса


    def fill_all_fields(self):
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
class CheckBoxPage(BasePage):

    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.remove_footer()
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTONS).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0: #проходимся по списку єлементов и рандомно кликаем
            item = item_list[random.randint(1,15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                print(item)
                count -= 1
            else:
                break
    #Не нужно видеть элементы, достаточно что бы они были в дом дереве
    def get_checked_ckeckboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS) #получаем выбранные жлементы
        data = []#создание буфера для отбора необходимых title и добавление их в список

        for box in checked_list: #проходимся по массиву, и элемент который выбран, нужно брать от туда текст

            title_item = box.find_element("xpath", self.locators.TITLE_ITEM) # Получаем текст по XPATH

            data.append(title_item.text)
        return str(data).replace(' ','').replace('doc','').replace('.','').lower()

    # Берем output data
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)  # получаем вібранные жлементы
        data = []  # создание буфера для отбора необходимых title и добавление их в список
        for item in result_list:  # проходимся по массиву, и элемент который выбран, нужно брать от туда текст

            data.append(item.text)
        return str(data).replace(' ','').lower()

class RadioButtonPage(BasePage): #наследуемся от BasePage.т.е - методы поиска элементов на странице и иницализация
    # Кликаем на элемент, появляется инфа что выбран элемент. Тайтлы кнопок одинаковые, формат одинаковый
    locators = RadioButtonPageLocators()
    def click_on_the_radio_button(self,choice): #аргумент choice это словарик с ключами

        choices = {'yes': self.locators.YES_RADIOBUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                   'no': self.locators.NO_RADIOBUTTON}

        #Выбор элемента для клика
        self.element_is_visible(choices[choice]).click()
    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text

class WebTablePage(BasePage):

    locators= WebTablePageLocators()

    def add_new_person(self):

        count = 1
        while count !=0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_clickable(self.locators.SUBMIT).click()
            count -=1
            return [firstname, lastname, str(age), email, str(salary), department]


    def check_new_added_person(self):

        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        #берём данные с этого списка пользоватетелей
        data = []
        for item in people_list:
            data.append(item.text.splitlines()) # убрираем переносы строк с помощью splitlines(), получаем отдельные массивы
        return data

    # Создание функции для поиска человека в таблице юзеров

    def search_some_person(self, key_word):

        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):

        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.locators.ROW_PARENT)
        return row.text.splitlines()


    # Создаем метод клика по карандашу edit на изменения возраста
    def update_person_info(self):

        person_info = next(generated_person())
        age = person_info.age #Берём сгенерированый возраст
        self.element_is_visible(self.locators.UPDATE_BUTTON).click() # нажимаем на карандаш
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age) # меняем возраст
        self.element_is_visible(self.locators.SUBMIT).click() #нажимаем сабмит
        return str(age)

    def delete_person(self):


        self.element_is_visible(self.locators.DELETE_BUTTON).click()

        #вытягиеваем текст который говорит что страница не найдена
    def check_deleted(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    # Есть значения колисчества строк в тблице которые мы заносим в цикл, где по очереди проходится, и записывать кол-во элементов в массив
    def select_up_to_some_rows(self):
        count = [5,10,20,25,50,100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"]')).click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)












