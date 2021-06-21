from fastapi import APIRouter, Depends
from typing import List
from .apischema import ApiUserSelect, ApiUserCreate, ApiUserUpdate
from database.models import User
from Domain.User.User import User as UserDomain
from Domain.Exception.DomainException import DomainException
from Domain.Exception.ExceptionHandler import ExceptionHandler
from Domain.Repository.dependences import get_user

router = APIRouter()


@router.get('/users', response_model=List[ApiUserSelect])
async def all(domain: UserDomain = Depends(get_user)):
    return await domain.all()


@router.get('/users/{user_id}', response_model=ApiUserSelect)
async def get(user_id: int, domain: UserDomain = Depends(get_user)):
    return await domain.get(user_id)


@router.put('/users/{user_id}', response_model=ApiUserSelect)
def update(user: ApiUserUpdate, domain: UserDomain = Depends(get_user)):
    print(user)


@router.post('/users/create', response_model=ApiUserSelect)
async def create(user: ApiUserCreate, domain: UserDomain = Depends(get_user)):
    try:
        id = await domain.create(user)
    except DomainException as e:
        ExceptionHandler.handle(e)
