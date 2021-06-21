from route.user import ApiUserCreate, ApiUserSelect
from typing import List
from .CreateUser import CreateUser
from Domain.Repository.User import User as UserRepository
from Domain.User.CreateValidator import CreateValidator
from .CreateValidator import CreateValidator


class User:
    def __init__(self):
        self.repository = UserRepository()

    async def all(self) -> List[ApiUserSelect]:
        users = await self.repository.all()
        userList = list()
        for user in users:
            userList.append(self.dict(user))
        return userList

    async def create(self, user: ApiUserCreate) -> int:
        CreateValidator.validate(user)
        creator = CreateUser(user)
        return await creator.create()

    async def get(self, user_id: int) -> ApiUserSelect:
        result = await self.repository.get(user_id)
        print(result)
        return self.dict(self.dict(result))

    def dict(self, user) -> ApiUserSelect:
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "memo": user.memo,
            "image": user.image,
            "created_at": user.created_at,
            "updated_at": user.updated_at
        }
