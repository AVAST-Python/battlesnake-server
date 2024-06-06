from flask import Blueprint, current_app, jsonify, request
import random

from .code_storage import code  # Code repository

move = Blueprint('move', __name__)

def pick_direction():
    directions = ["up", "down", "right", "left"]
    return random.choice(directions)

@move.route('/<string:user>/move', methods=['POST'])
def create_chat(user):
    current_app.logger.info(f'Moving request for {user}')
    data = request.get_json()
    current_app.logger.debug(f'Game data: {data}')
    response = {
        "move": pick_direction(),
    }
    return jsonify(response)
