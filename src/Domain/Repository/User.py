from database.models import User as UserModel
from Domain.Repository.Repository import Repository
from database.dbschema import users
from route.user import ApiUserCreate
from datetime import datetime


class User(Repository):

    def __init__(self):
        super().__init__()

    async def all(self):
        query = users.select()
        return await self.database.fetch_all(query)

    async def get(self, user_id: int):
        query = users.select().where(users.c.id == user_id)
        result = await self.database.execute(query)
        for r in result:
            print(r)

    async def create(self, user: ApiUserCreate):
        insert = users.insert()
        id = await self.database.execute(insert, {
            "name": user.name,
            "email": user.email,
            "memo": user.memo,
            "image": user.image,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        })
        return id
