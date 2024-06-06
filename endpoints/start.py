from flask import Blueprint, jsonify, request
from .code_storage import code  # Code repository

start = Blueprint('start', __name__)

@start.route('/<string:user>/start', methods=['POST'])
def create_chat(user):
    # The response will be ignored
    return f'Starting game for {user}!'
