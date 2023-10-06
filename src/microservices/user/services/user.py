import jwt

class UserService:

    def save(user):
        #como no va la base de datos no he añadido el codigo pero sería
        #similar al codigo usado para guardar el match
        return (200, "Guardamos el usuario en la base de datos.")

    def generateJWT(user, secret_key):
        payload = {"identity": user["username"]}
        token = jwt.encode(payload, secret_key, algorithm="HS256")
        return token
