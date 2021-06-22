from database.models import User as UserDb
from route.user import ApiUserCreate, ApiUserUpdate
from sqlalchemy.future import select
from sqlalchemy import update
from sqlalchemy.orm import Session
from datetime import datetime


class User:

    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def all(self):
        query = await self.db_session.execute(select(UserDb))
        result = list()
        for row in query.scalars():
            result.append(row.__dict__)
        return result

    async def get(self, user_id: int):
        result = await self.db_session.execute(
            select(UserDb).where(UserDb.id == user_id))
        return result.scalars().one().__dict__

    async def create(self, user: ApiUserCreate):
        new_user = UserDb(name=user.name, email=user.email,
                          memo=user.memo, image=user.image)
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user.id

    async def update(self, user: ApiUserUpdate):
        # クエリ生成
        query = update(UserDb).where(UserDb.id == user.id)
        query = query.values(name=user.name)
        query = query.values(email=user.email)
        query = query.values(memo=user.memo)
        query = query.values(image=user.image)
        query = query.values(updated_at=datetime.now())

        query.execution_options(synchronize_session="fetch")
        await self.db_session.execute(query)
