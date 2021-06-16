import databases
import sqlalchemy
import os

SHCEMA = 'mysql'
USER = os.environ['MYSQL_USER']
PASSWORD = os.environ['MYSQL_PASSWORD']
HOST = 'mysql'
PORT = os.environ['DB_PORT']
DB_NAME = os.environ['MYSQL_DATABASE']

DATABASE_URL = '{}://{}:{}@{}:{}/{}'.format(
    SHCEMA, USER, PASSWORD, HOST, PORT, DB_NAME)
database = databases.Database(DATABASE_URL, min_size=5, max_size=20)
ECHO_LOG = False

engine = sqlalchemy.create_engine(DATABASE_URL, echo=ECHO_LOG)
metadata = sqlalchemy.MetaData()
