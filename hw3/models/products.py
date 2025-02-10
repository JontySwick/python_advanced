from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Numeric
from hw3.models.abstract_model import AbstractModel


class Product(AbstractModel):
    name = Column(String(100), nullable=False, unique=True)
    price = Column(Numeric(10, 2), nullable=False)
    in_stock = Column(Boolean, nullable=False)
    # Задача 5: Установите связь между таблицами Product и Category с помощью колонки category_id.
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
