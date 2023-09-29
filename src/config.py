import os

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOSTNAME = os.getenv('DB_HOSTNAME')
DB_PORT = os.getenv('DB_PORT')

SQLALCHEMY_DATABASE_URI = 'postgresql://DB_USER:DB_PASSWORD@DB_HOSTNAME:DB_PORT/tic-tac-toe-db'
