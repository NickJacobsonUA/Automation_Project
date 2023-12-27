import random
import time

from pages.forms_page import FormPage
from conftest import driver


class TestForms:

    class TestPracticeForm:

        def test_form(self, driver):
            forms_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            forms_page.open()
            p = forms_page.fill_form_fields() # помещаем данные заполненные в форме в переменную
            result = forms_page.form_result() # помещаем данные взятые из формы в переменную
            print(p.firstname, p.lastname, p.email)
            print(result[0], result[1])
            assert [p.firstname + " " + p.lastname, p.email] == [result[0], result[1]], "the form has not been filled"


