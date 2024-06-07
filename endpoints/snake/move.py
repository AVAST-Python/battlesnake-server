from flask import Blueprint, current_app, jsonify, request
import random

from ..code_storage import users_compiled_function

move = Blueprint('move', __name__)

def pick_direction():
    directions = ["up", "down", "right", "left"]
    return random.choice(directions)

@move.route('/snake/<string:user>/move', methods=['POST'])
def create_chat(user):

    current_app.logger.info(f'Moving request for {user}')

    user_function = users_compiled_function.get(user)
    if user_function is None:
        current_app.logger.error(f'No code found for {user}')
        return jsonify({"error": "No code found for user"}), 400

    data = request.get_json()
    current_app.logger.debug(f'Game data: {data}')

    res = user_function(data)
    response = {
        "move": res,
    }
    return jsonify(response)
