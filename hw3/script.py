from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from hw3.models.abstract_model import AbstractModel
from hw3.models.category import Category
from hw3.models.products import Product

# Задача 1: Создайте экземпляр движка для подключения к SQLite базе данных в памяти.
engine = create_engine('sqlite:///:memory:')
AbstractModel.metadata.create_all(engine)

# Задача 2: Создайте сессию для взаимодействия с базой данных, используя созданный движок.
with Session(engine) as session, session.begin():
    # Задача 3: Определите модель продукта Product со следующими типами колонок:
    product = Product(
        name='Fake product',
        price=123.45,
        in_stock=True,
        category_id=1,
    )

    # Задача 4: Определите связанную модель категории Category со следующими типами колонок:
    category = Category(
        name='Fake category',
    )

    session.add_all([product, category])



