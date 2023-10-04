import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_HOST = os.getenv('DB_HOSTNAME')
DB_PORT = os.getenv('DB_PORT',5432)

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

DB_NAME = os.getenv('DB_USER')

DB_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

PERM = os.getenv('PERM')

engine = create_engine(
    DB_URI,
    connect_args={'ssl_ca': PERM}
)
Session = sessionmaker(bind=engine)
session = Session()