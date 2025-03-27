from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from app.models import Question, db
from app.schemas.questions import QuestionCreate, QuestionResponse

questions_bp = Blueprint('questions', __name__, url_prefix='/questions')


@questions_bp.route('/', methods=['GET'])
def get_questions():
    """Получение списка всех вопросов."""
    # Используем SQLAlchemy ORM для загрузки всех вопросов
    questions = Question.query.all()
    # Преобразуем список объектов вопросов в список словарей
    questions_data = [QuestionResponse.model_validate(question).model_dump() for question in questions]

    return jsonify(questions_data)


@questions_bp.route('/', methods=['POST'])
def create_question():
    """Создание нового вопроса."""
    data = request.get_json()
    try:
        question_data = QuestionCreate(**data)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    question = Question(text=question_data.text)
    db.session.add(question)
    db.session.commit()

    return jsonify(QuestionResponse(id=question.id, text=question.text).model_dump()), 201


@questions_bp.route('/<int:id>', methods=['GET'])
def get_question(id):
    """Получение деталей конкретного вопроса по его ID."""
    question = Question.query.get(id)
    if question is None:
        return jsonify({'message': "Вопрос с таким ID не найден"}), 404

    return jsonify({'message': f"Вопрос: {question.text}"}), 200


@questions_bp.route('/<int:id>', methods=['PUT'])
def update_question(id):
    """Обновление конкретного вопроса по его ID."""
    question = Question.query.get(id)
    if question is None:
        return jsonify({'message': "Вопрос с таким ID не найден"}), 404

    data = request.get_json()
    if 'text' in data:
        question.text = data['text']
        db.session.commit()
        return jsonify({'message': f"Вопрос обновлен: {question.text}"}), 200
    else:
        return jsonify({'message': "Текст вопроса не предоставлен"}), 400


@questions_bp.route('/<int:id>', methods=['DELETE'])
def delete_question(id):
    """Удаление конкретного вопроса по его ID."""
    question = Question.query.get(id)
    if question is None:
        return jsonify({'message': "Вопрос с таким ID не найден"}), 404

    db.session.delete(question)
    db.session.commit()

    return jsonify({'message': f"Вопрос с ID {id} удален"}), 200
