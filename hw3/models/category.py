from sqlalchemy import Column, String
from hw3.models.abstract_model import AbstractModel


class Category(AbstractModel):
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(500))
