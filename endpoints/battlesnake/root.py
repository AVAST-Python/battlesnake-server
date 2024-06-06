from flask import Blueprint, jsonify

root = Blueprint('root', __name__)

# Root endpoint
@root.route('/<string:user>/', methods=['GET'])
def index(user):
    response = {
        "apiversion": "1",
        "author": user,
        "color": "#888888",
        "head": "default",
        "tail": "default",
        "version": "0.0.1-beta"
    }
    return jsonify(response)
