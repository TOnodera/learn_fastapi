import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    image: str
    memo: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class Article(BaseModel):
    id: int
    title: str
    body: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
