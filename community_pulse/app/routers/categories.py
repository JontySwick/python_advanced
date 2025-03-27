from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from app.models import Category, db
from app.schemas.questions import CategoryBase

categories_bp = Blueprint('categorys', __name__, url_prefix='/categories')


@categories_bp.route('/', methods=['GET'])
def get_categorys():
    """Получение списка всех вопросов."""
    # Используем SQLAlchemy ORM для загрузки всех вопросов
    categorys = Category.query.all()
    # Преобразуем список объектов вопросов в список словарей
    categorys_data = [CategoryBase.model_validate(category).model_dump() for category in categorys]

    return jsonify(categorys_data)


@categories_bp.route('/', methods=['POST'])
def create_category():
    """Создание нового вопроса."""
    data = request.get_json()
    try:
        category_data = CategoryBase(**data)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    category = Category(text=category_data.text)
    db.session.add(category)
    db.session.commit()

    return jsonify(CategoryBase(id=category.id, text=category.text).model_dump()), 201

@categories_bp.route('/<int:id>', methods=['PUT'])
def update_category(id):
    """Обновление конкретного вопроса по его ID."""
    category = Category.query.get(id)
    if category is None:
        return jsonify({'message': "Вопрос с таким ID не найден"}), 404

    data = request.get_json()
    if 'text' in data:
        category.text = data['text']
        db.session.commit()
        return jsonify({'message': f"Вопрос обновлен: {category.text}"}), 200
    else:
        return jsonify({'message': "Текст вопроса не предоставлен"}), 400


@categories_bp.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    """Удаление конкретного вопроса по его ID."""
    category = Category.query.get(id)
    if category is None:
        return jsonify({'message': "Вопрос с таким ID не найден"}), 404

    db.session.delete(category)
    db.session.commit()

    return jsonify({'message': f"Вопрос с ID {id} удален"}), 200
