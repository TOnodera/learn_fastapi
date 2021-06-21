from pydantic import BaseModel
from datetime import datetime


class ApiUserSelect(BaseModel):
    id: int
    name: str
    email: str
    memo: str
    image: str
    created_at: datetime
    updated_at: datetime


class ApiUserCreate(BaseModel):
    name: str
    email: str
    memo: str
    image: str


class ApiUserUpdate(BaseModel):
    id: int
    name: str
    email: str
    memo: str
    image: str
