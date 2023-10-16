#lesson 4.1
import random

from data.data import Person
from faker import Faker


faker_ru = Faker('ru_Ru') #Генерация данных на русском
fake = Faker('en_US') # Генерация данных на английском
Faker.seed()

def generated_person():
    yield Person(
        full_name = fake.name() + " " + fake.last_name() + " " + fake.name(),
        firstname= fake.name(),
        lastname= fake.last_name(),
        age=random.randint(10,80),
        department=fake.job(),
        salary=random.randint(10000,100000),
        email = fake.email(),
        current_address = fake.street_address(),
        permanent_address = fake.street_address(),
    )