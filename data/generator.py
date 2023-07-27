from faker import Faker

class GeneratedData:

    def generate_first_name():
        fake = Faker('ru_RU')
        first_name = fake.first_name()
        return first_name

    def generate_last_name():
        fake = Faker('ru_RU')
        last_name = fake.last_name()
        return last_name

    def generate_address():
        fake = Faker('ru_RU')
        address = f"{fake.street_name()} {str(fake.random_int(111, 999))}"
        return address

    def generate_phone_number():
        fake = Faker('ru_RU')
        phone_number = fake.phone_number('+79#########')
        return phone_number
