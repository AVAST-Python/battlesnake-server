from flask import Blueprint, jsonify, request
from .code_storage import code  # Code repository

move = Blueprint('move', __name__)

@move.route('/<string:user>/move', methods=['POST'])
def create_chat(user):
    # return f'Hello, {user}!'
    return 'right'
