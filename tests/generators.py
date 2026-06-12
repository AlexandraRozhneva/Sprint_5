import random
import string

def generate_email():
    """Генерирует email в формате имя_фамилия_номер_когорты_3_цифры@yandex.ru"""
    name = "Alexandra"
    surname = "Rozhneva"
    cohort = "48666"
    random_digits = ''.join(random.choices(string.digits, k=3))
    
    email = f"{name}_{surname}_{cohort}_{random_digits}@yandex.ru"
    return email

def generate_password(min_length=6):
    """Генерирует случайный пароль"""
    length = random.randint(min_length, 12)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def generate_name():
    """Генерирует случайное имя"""
    names = ["Александр", "Мария", "Иван", "Елена", "Дмитрий", "Анна"]
    return random.choice(names)

def generate_invalid_password():
    """Генерирует некорректный пароль (менее 6 символов)"""
    length = random.randint(1, 5)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))