from flask import Blueprint, jsonify, request

root = Blueprint('root', __name__)

# Root endpoint
@root.route('/', methods=['GET'])
def create_chat():
    return "Battlesnake server is running!"
