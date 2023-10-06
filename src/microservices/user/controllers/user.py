from flask_restx import Namespace, Resource
from src.microservices.user.services.user import UserService
from src.microservices.user.dto.user import user_model
import uuid

user_api = Namespace('match', description='Operaciones de Juego')

@user_api.route('/move')
class login(Resource):
    @user_api.expect(user_model)
    def post(self):
        """
        This endpoint allow to login.
        """
        try:
            data = user_api.payload
            data["userId"] = str(uuid.uuid4())
            UserService.save(data)
            token = UserService.generateJWT(data)
            return token
        except Exception as e:
            return(500, f"An error occurred: {str(e)}")
