from flask import Blueprint, current_app, jsonify, request
from .code_storage import code  # Code repository

start = Blueprint('start', __name__)

@start.route('/<string:user>/start', methods=['POST'])
def create_chat(user):
    data = request.get_json()
    current_app.logger.info(f'Starting game for {user}')
    current_app.logger.debug(f'Game data: {data}')

    # The response will be ignored
    return f'Starting game for {user}!'
