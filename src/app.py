from flask import Flask
from .microservices/match/controllers/match import match_api

app = Flask(__name__)

app.register_blueprint(match_api, url_prefix='/juan')

@app.route('/')
def hello():
    return '¡Hola, mundo!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
