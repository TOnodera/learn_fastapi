from fastapi import APIRouter
from typing import List
from .schema import UserSelect, UserCreate
from database.config import connection
from database.models import User
from Domain.User.User import User as UserDomain

router = APIRouter()
domain = UserDomain()


@router.get('/users', response_model=List[UserSelect])
def all():
    return domain.all()


@router.post('/users/create', response_model=UserSelect)
def create(user: UserCreate):
    id = domain.create(user)
    orm = User()
    return orm.query.get(id).toDict()
