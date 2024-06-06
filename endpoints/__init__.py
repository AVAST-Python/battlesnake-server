from flask import Blueprint
from .root import root
from .start import start
from .move import move

# Register blueprints for chats endpoints
snake = Blueprint('snake', __name__)
snake.register_blueprint(root)
snake.register_blueprint(start)
snake.register_blueprint(move)
