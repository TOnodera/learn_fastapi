from fastapi import APIRouter
from typing import List
from .apischema import ApiUserSelect, ApiUserCreate, ApiUserUpdate
from database.models import User
from Domain.User.User import User as UserDomain
from Domain.Exception.DomainException import DomainException
from Domain.Exception.ExceptionHandler import ExceptionHandler

router = APIRouter()
domain = UserDomain()


@router.get('/users', response_model=List[ApiUserSelect])
async def all():
    return await domain.all()


@router.get('/users/{user_id}', response_model=ApiUserSelect)
async def get(user_id: int):
    return await domain.get(user_id)


@router.put('/users/{user_id}', response_model=ApiUserSelect)
def update(user: ApiUserUpdate):
    print(user)


@router.post('/users/create', response_model=ApiUserSelect)
async def create(user: ApiUserCreate):
    try:
        id = await domain.create(user)

        print(id)
    except DomainException as e:
        ExceptionHandler.handle(e)
