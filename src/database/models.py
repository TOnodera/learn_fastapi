import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from .config import Base, ENGINE, TEST_ENGINE
from datetime import datetime


class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(200))
    email = Column('email', String(255))
    image = Column('image', String(255))
    memo = Column('memo', Text)
    created_at = Column('created_at', DateTime,
                        default=datetime.now, nullable=False)
    updated_at = Column('updated_at', DateTime,
                        default=datetime.now, nullable=False)

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'image': self.image,
            'memo': self.memo,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


class Article(Base):
    __tablename__ = 'articles'
    id = Column('id', Integer, primary_key=True)
    title = Column('title', String(200))
    body = Column('body', Text)
    created_at = Column('created_at', DateTime,
                        default=datetime.now, nullable=False)
    updated_at = Column('updated_at', DateTime,
                        default=datetime.now, nullable=False)


def create(args):
    # DB作成
    Base.metadata.create_all(bind=ENGINE)
    # テストDB作成
    Base.metadata.create_all(bind=TEST_ENGINE)


def drop():
    Base.metadata.drop_all(bind=ENGINE)
    Base.metadata.drop_all(bind=TEST_ENGINE)


if __name__ == "__main__":
    drop()
    create(sys.argv)
