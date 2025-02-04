from sqlalchemy import Column, Integer
from sqlalchemy.orm import declared_attr, DeclarativeBase


class AbstractModel(DeclarativeBase):
    id = Column(Integer, primary_key=True, autoincrement=True)

    @classmethod
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
