from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
import os

DATABASE_URL = 'mysql+aiomysql://%s:%s@%s:%s/%s?charset=utf8' % (
    os.environ['MYSQL_USER'],
    os.environ['MYSQL_PASSWORD'],
    'mysql',
    os.environ['MYSQL_PORT'],
    os.environ['MYSQL_DATABASE']
)

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()
