from flask import Blueprint, current_app, jsonify, request
from .code_storage import code  # Code repository

end = Blueprint('end', __name__)

@end.route('/<string:user>/end', methods=['POST'])
def create_chat(user):
    data = request.get_json()
    game_id = data.get("game", {}).get("id")

    current_app.logger.info(f'Game {game_id} ended for {user}')
    current_app.logger.debug(f'Game data: {data}')
    
    # The response will be ignored
    return f'Finished game {game_id} for {user}!'
