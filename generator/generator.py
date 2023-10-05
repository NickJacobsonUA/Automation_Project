#lesson 4.1
from data.data import Person
from faker import Faker


faker_ru = Faker('ru_Ru') #Генерация данных на русском
fake = Faker('en_US') # Генерация данных на английском
Faker.seed()

def generated_person():
    yield Person(
        full_name = fake.name() + " " + fake.last_name() + " " + fake.name(),
        email = fake.email(),
        current_address = fake.street_address(),
        permanent_address = fake.street_address(),
    )