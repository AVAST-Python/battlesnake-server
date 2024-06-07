from flask import Blueprint

# Register blueprints for chats endpoints
from .battlesnake.root import root
from .battlesnake.start import start
from .battlesnake.move import move
from .battlesnake.end import end

snake = Blueprint('snake', __name__)
snake.register_blueprint(root)
snake.register_blueprint(start)
snake.register_blueprint(move)
snake.register_blueprint(end)

# Register blueprints for user endpoints
from .user.user_login import user_login

user = Blueprint('user', __name__)
user.register_blueprint(user_login)
