from flask import Blueprint, jsonify

match_api = Blueprint('match_api', __name__)

@match_api.route('/match', methods=['GET'])
def obtener_servicio1():
    data = {
        'mensaje': 'todo correcto',
        'descripcion': 'Estas ejecutando un GET.'
    }
    return jsonify(data)
