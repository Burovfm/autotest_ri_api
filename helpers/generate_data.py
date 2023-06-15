from faker import Faker

faker = Faker(locale="ru_RU")


def generate_text(max_chars, min_chars=1) -> str:
    return faker.pystr(min_chars=min_chars, max_chars=max_chars)


def generate_uuid() -> str:
    return faker.uuid4()
