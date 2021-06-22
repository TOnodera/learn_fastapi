from fastapi import APIRouter, Depends, File, UploadFile
from typing import List
from route.apischema import ApiUserSelect, ApiUserCreate, ApiUserUpdate
from database.models import User
from Domain.User.User import User as UserDomain
from Domain.Exception.DomainException import DomainException
from Domain.Exception.ExceptionHandler import ExceptionHandler
from Domain.Repository.dependences import get_user
import aiofiles
import config
import uuid

router = APIRouter()


@router.get('/users', response_model=List[ApiUserSelect])
async def all(domain: UserDomain = Depends(get_user)):
    return await domain.all()


@router.get('/users/{user_id}', response_model=ApiUserSelect)
async def get(user_id: int, domain: UserDomain = Depends(get_user)):
    return await domain.get(user_id)


@router.put('/users/{user_id}', response_model=ApiUserSelect)
async def update(user: ApiUserUpdate, domain: UserDomain = Depends(get_user)):
    return await domain.update(user)


@router.post('/users/create', response_model=ApiUserSelect)
async def create(user: ApiUserCreate, domain: UserDomain = Depends(get_user)):
    try:
        return await domain.create(user)
    except DomainException as e:
        ExceptionHandler.handle(e)


@router.post("/users/create/image")
async def create_image(id: int, file: UploadFile = File(...)):

    ext = file.filename.split(".")[-1]
    async with aiofiles.open("/home/python/workspace/src/store/"+"USER_"+id+"."+ext, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)
    return {"result": "OK"}
