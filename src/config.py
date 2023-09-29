import os

DB_USER = os.getenv('DB_USER')
print("DB_USER:", DB_USER)
DB_PASSWORD = os.getenv('DB_PASSWORD')
print("DB_PASSWORD:", DB_PASSWORD)
DB_HOSTNAME = os.getenv('DB_HOSTNAME')
print("DB_HOSTNAME:", DB_HOSTNAME)
DB_PORT = os.getenv('DB_PORT',5432)
print("DB_PORT:", DB_PORT)

SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/tic-tac-toe-db'
