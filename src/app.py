from flask import Flask
from microservices.match.controller.match import match_api

tic_tac_toe = Flask(__name__)

tic_tac_toe.register_blueprint(match_api, url_prefix='/')

if __name__ == '__main__':
    tic_tac_toe.run(host='127.0.0.1', port=5000)
