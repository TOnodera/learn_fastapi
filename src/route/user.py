from fastapi import APIRouter
from typing import List
from .apischema import UserSelect, UserCreate
from database.models import User
from Domain.User.User import User as UserDomain
from Domain.Exception.DomainException import DomainException
from Domain.Exception.ExceptionHandler import ExceptionHandler

router = APIRouter()
domain = UserDomain()


@router.get('/users', response_model=List[UserSelect])
def all():
    return domain.all()


@router.post('/users/create', response_model=UserSelect)
def create(user: UserCreate):
    try:
        id = domain.create(user)
        orm = User()
        return orm.query.get(id).toDict()
    except DomainException as e:
        ExceptionHandler.handle(e)
