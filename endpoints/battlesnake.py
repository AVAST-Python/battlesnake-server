from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Battlesnake server is running!"

@app.route("/start", methods=["POST"])
def start():
    data = request.get_json()
    response = {
        "color": "#888888",
        "headType": "default",
        "tailType": "default"
    }
    return jsonify(response)

@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    # For simplicity, just move 'up'
    response = {
        "move": "up"
    }
    return jsonify(response)

@app.route("/end", methods=["POST"])
def end():
    data = request.get_json()
    return "Game Over!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
