import sqlalchemy
import databases
import os
import datetime

DATABASE_URL = 'mysql://%s:%s@%s:%s/%s?charset=utf8' % (
    os.environ['MYSQL_USER'],
    os.environ['MYSQL_PASSWORD'],
    'mysql',
    os.environ['MYSQL_PORT'],
    os.environ['MYSQL_DATABASE']
)

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(255)),
    sqlalchemy.Column('email', sqlalchemy.String(255)),
    sqlalchemy.Column('image', sqlalchemy.String(255)),
    sqlalchemy.Column('memo', sqlalchemy.Text),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime,
                      default=datetime.datetime.now),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime,
                      default=datetime.datetime.now)
)

articles = sqlalchemy.Table(
    'articles',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('title', sqlalchemy.String(255)),
    sqlalchemy.Column('body', sqlalchemy.Text),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime,
                      default=datetime.datetime.now),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime,
                      default=datetime.datetime.now)
)


ENGINE = sqlalchemy.create_engine(DATABASE_URL)
metadata.drop_all(ENGINE)
metadata.create_all(ENGINE)
