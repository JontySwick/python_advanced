from pydantic import BaseModel, Field

# 1. Создать классы моделей данных с помощью Pydantic для пользователя и его адреса.
# * Address: Должен содержать следующие поля:
#   * city: строка, минимум 2 символа.
#   * street: строка, минимум 3 символа.
#   * house_number: число, должно быть положительным.
#
class Address(BaseModel):
    city: str = Field(..., pattern=r'^[\w\s]{2,}$')
    street: str = Field(None, pattern=r'^[\w\s]{3,}$')
    house_number: int = Field(None, gt=0)
