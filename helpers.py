import random
import string


def generate_email():
    # Генерация случайного email
    random_digits = ''.join(random.choices(string.digits, k=3))
    email = f"dmitriy_zyabikov_46_{random_digits}@yandex.ru"
    return email


def generate_password(length=6):
    # Генерация пароля
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(characters, k=length))
    return password


def generate_name():
    # Выбор случайного имени
    names = ['Дмитрий', 'Иван', 'Алексей', 'Сергей', 'Михаил', 'Андрей']
    return random.choice(names)
