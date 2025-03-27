from sqlalchemy.orm import Mapped, relationship

from app.models import db


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    question: Mapped["Question"] = relationship(back_populates="questions")

    def __repr__(self):
        return f'Category: {self.name}'
