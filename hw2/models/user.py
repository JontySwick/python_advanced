from pydantic import BaseModel, EmailStr, Field, field_validator
from pydantic_core.core_schema import ValidationInfo

from hw2.models.address import Address


# 1. Создать классы моделей данных с помощью Pydantic для пользователя и его адреса.
# * User: Должен содержать следующие поля:
#   * name: строка, должна быть только из букв, минимум 2 символа.
#   * age: число, должно быть между 0 и 120.
#   * email: строка, должна соответствовать формату email.
#   * is_employed: булево значение, статус занятости пользователя.
#   * address: вложенная модель адреса.
class User(BaseModel):
    name: str = Field(..., pattern=r'^[a-zA-Z]{2,10}$')
    age: int = Field(..., ge=0, le=120)
    email: EmailStr
    is_employed: bool
    address: Address

    @field_validator('is_employed')
    def validate_is_employed(cls, is_employed: bool, info: ValidationInfo) -> bool:
        # 3. Добавить кастомный валидатор для проверки соответствия возраста и статуса занятости пользователя.
        # * Проверка, что если пользователь указывает, что он занят (is_employed = true), его возраст должен быть от 18 до 65 лет.
        if is_employed and not 18 < info.data['age'] < 65:
            raise ValueError("User age must be between 18 and 65 years")

        return is_employed
