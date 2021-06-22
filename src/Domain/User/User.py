from route.user import ApiUserCreate, ApiUserSelect
from typing import List
from Domain.Repository.User import User as UserRepository
from Domain.User.Validator.CreateValidator import CreateValidator
from Domain.User.Validator.UpdateValidator import UpdateValidator
from sqlalchemy.orm import Session


class User:
    def __init__(self, db_session: Session):
        self.repository = UserRepository(db_session)

    async def all(self) -> List[ApiUserSelect]:
        users = await self.repository.all()
        result = list()
        for user in users:
            result.append(self.dict(user))
        return result

    async def create(self, user: ApiUserCreate) -> ApiUserSelect:
        CreateValidator.validate(user)
        id = await self.repository.create(user)
        return await self.get(id)

    async def update(self, user: ApiUserCreate) -> ApiUserSelect:
        UpdateValidator.validate(user)
        await self.repository.update(user)
        return await self.get(user.id)

    async def get(self, user_id: int) -> ApiUserSelect:
        result = await self.repository.get(user_id)
        return self.dict(self.dict(result))

    def dict(self, user) -> ApiUserSelect:
        return {
            "id": user['id'],
            "name": user['name'],
            "email": user['email'],
            "memo": user['memo'],
            "image": user['image'],
            "created_at": user['created_at'],
            "updated_at": user['updated_at']
        }
