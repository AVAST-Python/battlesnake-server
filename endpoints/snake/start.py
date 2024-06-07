from flask import Blueprint, current_app, jsonify, request
from ..debug_storage import execution_results

start = Blueprint('start', __name__)

@start.route('/snake/<string:user>/start', methods=['POST'])
def create_chat(user):
    data = request.get_json()
    current_app.logger.info(f'Starting game for {user}')
    current_app.logger.debug(f'Game data: {data}')

    # Clean the execution results for the user
    execution_results[user] = []

    # The response will be ignored
    return f'Starting game for {user}!'
