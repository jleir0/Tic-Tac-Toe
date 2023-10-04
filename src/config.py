import os 

DB_HOST = os.getenv('DB_HOSTNAME')
DB_PORT = os.getenv('DB_PORT',5432)

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

DB_NAME = os.getenv('DB_USER')

DB_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

