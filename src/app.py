from flask import Flask
from microservices.match.controller.match import match_api

app = Flask(__name__)

app.register_blueprint(match_api, url_prefix='/TicTacToe')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)