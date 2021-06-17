from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
import os

DATABASE = 'mysql://%s:%s@%s:%s/%s?charset=utf8' % (
    os.environ['MYSQL_USER'],
    os.environ['MYSQL_PASSWORD'],
    'mysql',
    os.environ['MYSQL_PORT'],
    os.environ['MYSQL_DATABASE']
)

ENGINE = create_engine(DATABASE, encoding="utf-8", echo=True)

connection = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
)

Base = declarative_base()
Base.query = connection.query_property()


# テスト用データベース
TEST_DATABASE = 'mysql://%s:%s@%s:%s/%s' % (
    os.environ['MYSQL_USER_TEST'],
    os.environ['MYSQL_PASSWORD_TEST'],
    'mysql_test',
    os.environ['MYSQL_PORT'],
    os.environ['MYSQL_DATABASE_TEST']
)


TEST_ENGINE = create_engine(TEST_DATABASE, encoding="utf-8", echo=True)

TEST_connection = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=TEST_ENGINE)
)
