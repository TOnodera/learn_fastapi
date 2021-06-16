from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
import os

DATABASE = 'mysql://%s:%s@%s:%s/%s' % (
    os.environ['MYSQL_USER'],
    os.environ['MYSQL_PASSWORD'],
    'mysql',
    os.environ['DB_PORT'],
    os.environ['MYSQL_DATABASE']
)

ENGINE = create_engine(DATABASE, encoding="utf-8", echo=True)

session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
)

Base = declarative_base()
Base.query = session.query_property()
