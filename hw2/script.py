# Разработать систему регистрации пользователя, используя Pydantic для валидации входных данных,
# обработки вложенных структур и сериализации. Система должна обрабатывать данные в формате JSON.
from pydantic import ValidationError
from hw2.models.user import User


# 1. Создать классы моделей данных с помощью Pydantic для пользователя и его адреса.

# 2. Реализовать функцию, которая принимает JSON строку, десериализует её в объекты Pydantic,
# валидирует данные, и в случае успеха сериализует объект обратно в JSON и возвращает его.
def persist_data(data: str) -> str|None:
    try:
        user = User.model_validate_json(data)
    except ValidationError as e:
        print(e)
    else:
        return user.model_dump_json(indent=4)


# 4. Написать несколько примеров JSON строк для проверки различных сценариев валидации:

# успешные регистрации
user = persist_data("""
    {
        "name": "John",
        "age": 60,
        "email": "john.doe@example.com",
        "is_employed": true,
        "address": {
            "city": "New York",
            "street": "5th Avenue",
            "house_number": 123
        }
    }
 """)
print(user)
# и случаи, когда валидация не проходит (например возраст не соответствует статусу занятости).
user = persist_data("""
    {
        "name": "Doe",
        "age": 11,
        "email": "john.doe@example.com",
        "is_employed": true,
        "address": {
            "city": "New York",
            "street": "5th Avenue",
            "house_number": 123
        }
    }
 """)

print(user)
