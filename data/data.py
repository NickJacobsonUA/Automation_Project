#lesson 4.1 - создание универсального дата класса Person который будет хранить данные человека
from dataclasses import dataclass



@dataclass

#прописываем тип свойств класса
class Person:
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None