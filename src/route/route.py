from fastapi import APIRouter
from typing import List
from .schema import UserSelect, UserCreate
from database.config import connection
from database.models import User

router = APIRouter()


@router.get('/users', response_model=List[UserSelect])
def all():
    users = connection.query(User).all()
    userList = []
    for user in users:
        userList.append(user.toDict())
    return userList


@router.post('/users/create', response_model=UserSelect)
def create(user: UserCreate):
    userOrm = User()
    userOrm.name = user.name
    userOrm.email = user.email
    connection.add(userOrm)
