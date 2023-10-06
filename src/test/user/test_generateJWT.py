import unittest
import jwt
from src.microservices.user.services.user import UserService

class TestGenerateJWT(unittest.TestCase):

    def test_generate_jwt(self):

        user = {}
        user["username"] = "test"

        token = UserService.generateJWT(user, "e0b38a2b2a1d1eac0b50a192e7f03268")

        info = jwt.decode(token, "e0b38a2b2a1d1eac0b50a192e7f03268", algorithms=["HS256"])
        self.assertEqual(info["identity"], user["username"])

if __name__ == '__main__':
    unittest.main()
