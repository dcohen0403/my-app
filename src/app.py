from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for players
players_data = [
    {"id": 1, "name": "Player 1", "score": 100},
    {"id": 2, "name": "Player 2", "score": 150},
    {"id": 3, "name": "Player 3", "score": 120},
]

@app.route('/getplayers', methods=['GET'])
def get_players():
    return jsonify(players_data)

if __name__ == '__main__':
    app.run(debug=True)