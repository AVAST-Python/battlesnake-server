from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

from endpoints import snake

app = Flask(__name__)

# Allow CORS for local development
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:*"}})

# Register endpoints
app.register_blueprint(snake)

if __name__ == '__main__':
    app.run(debug=True)
