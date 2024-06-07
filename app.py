from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
import logging

load_dotenv()

from endpoints import snake
from endpoints import user

app = Flask(__name__)

# Basic logging configuration
log_level = os.getenv('LOG_LEVEL', 'DEBUG')
logging.basicConfig(level=log_level)

# Allow CORS for local development
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:*"}})

# Register endpoints
app.register_blueprint(snake)
app.register_blueprint(user)

if __name__ == '__main__':
    # app.run(debug=True, port=8080)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host="0.0.0.0", port=8000, debug=True)
