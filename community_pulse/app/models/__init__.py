from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from app.models.response import *
from app.models.questions import *
from app.models.categories import *
