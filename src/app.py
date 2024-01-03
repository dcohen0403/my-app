from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Sample data for players
df = pd.read_csv("premierLeagueDatabase.csv")

@app.route('/getplayers', methods=['GET'])
def get_players():
    return df.to_json()

if __name__ == '__main__':
    app.run(debug=True)