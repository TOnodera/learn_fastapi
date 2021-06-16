import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from config import Base, ENGINE, TEST_ENGINE
from datetime import datetime


class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(200))
    age = Column('email', String(255))
    created_at = Column('created_at', DateTime,
                        default=datetime.now, nullable=False)
    updated_at = Column('updated_at', DateTime,
                        default=datetime.now, nullable=False)


class Article(Base):
    __tablename__ = 'articles'
    id = Column('id', Integer, primary_key=True)
    title = Column('title', String(200))
    body = Column('body', Text)
    created_at = Column('created_at', DateTime,
                        default=datetime.now, nullable=False)
    updated_at = Column('updated_at', DateTime,
                        default=datetime.now, nullable=False)


def main(args):
    Base.metadata.create_all(bind=ENGINE)
    Base.metadata.create_all(bind=TEST_ENGINE)


if __name__ == "__main__":
    main(sys.argv)
