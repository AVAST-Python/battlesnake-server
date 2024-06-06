from flask import Blueprint
from .root import root

# Register blueprints for chats endpoints
snake = Blueprint('snake', __name__)
snake.register_blueprint(root)
