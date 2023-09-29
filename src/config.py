import os

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOSTNAME = os.getenv('DB_HOSTNAME')
DB_PORT = 5432

SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/tic-tac-toe-db'
