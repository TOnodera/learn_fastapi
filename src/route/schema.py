from pydantic import BaseModel
from datetime import datetime


class UserSelect(BaseModel):
    id: int
    name: str
    email: str
    memo: str
    image: str
    created_at: datetime
    updated_at: datetime


class UserCreate(BaseModel):
    name: str
    email: str
    memo: str
    image: str
