from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from hw3.models.abstract_model import AbstractModel
from hw3.models.category import Category
from hw3.models.products import Product

# Задача 1: Наполнение данными
# Добавьте в базу данных следующие категории и продукты
engine = create_engine('sqlite:///:memory:')
AbstractModel.metadata.create_all(engine)

with Session(engine) as session, session.begin():
    models = []
    # Добавление категорий: Добавьте в таблицу categories следующие категории:
    # Название: "Электроника", Описание: "Гаджеты и устройства."
    models.append(Category(
        name='Электроника',
        description='Гаджеты и устройства',
    ))

    # Название: "Книги", Описание: "Печатные книги и электронные книги."
    models.append(Category(
        name='Книги',
        description='Печатные книги и электронные книги.',
    ))

    # Название: "Одежда", Описание: "Одежда для мужчин и женщин."
    models.append(Category(
        name='Одежда',
        description='Одежда для мужчин и женщин.',
    ))

    # Добавление продуктов: Добавьте в таблицу products следующие продукты, убедившись, что каждый продукт связан с соответствующей категорией:

    # Название: "Смартфон", Цена: 299.99, Наличие на складе: True, Категория: Электроника
    models.append(Product(
        name='Смартфон',
        price=299.99,
        in_stock=True,
        category_id=1,
    ))

    # Название: "Ноутбук", Цена: 499.99, Наличие на складе: True, Категория: Электроника
    models.append(Product(
        name='Ноутбук',
        price=499.99,
        in_stock=True,
        category_id=1,
    ))

    # Название: "Научно-фантастический роман", Цена: 15.99, Наличие на складе: True, Категория: Книги
    models.append(Product(
        name='Научно-фантастический роман',
        price=15.99,
        in_stock=True,
        category_id=2,
    ))

    # Название: "Джинсы", Цена: 40.50, Наличие на складе: True, Категория: Одежда
    models.append(Product(
        name='Джинсы',
        price=40.50,
        in_stock=True,
        category_id=3,
    ))

    # Название: "Футболка", Цена: 20.00, Наличие на складе: True, Категория: Одежда
    models.append(Product(
        name='Футболка',
        price=20.00,
        in_stock=True,
        category_id=3,
    ))

    session.add_all(models)
