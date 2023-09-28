from flask_restx import Namespace, Resource

match_api = Namespace('match', description='Operaciones de Juego')

@match_api.route('/')
class MatchResource(Resource):
    def get(self):
        """
        Obtiene información sobre los juegos.

        Descripción adicional si es necesaria.
        """
        return {'mensaje': 'Todo correcto', 'descripcion': 'Obteniendo información sobre los juegos'}
