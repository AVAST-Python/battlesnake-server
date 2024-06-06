from flask import Blueprint
from .battlesnake.root import root
from .battlesnake.start import start
from .battlesnake.move import move
from .battlesnake.end import end

# Register blueprints for chats endpoints
snake = Blueprint('snake', __name__)
snake.register_blueprint(root)
snake.register_blueprint(start)
snake.register_blueprint(move)
snake.register_blueprint(end)
