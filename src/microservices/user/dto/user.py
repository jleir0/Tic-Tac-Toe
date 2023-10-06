from flask_restx import fields

user_model = {
    'userName': fields.String(description='Username.'),
    'password': fields.String(description='Password.'),
}
