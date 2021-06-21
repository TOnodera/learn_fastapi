from database.models import User as UserDb
from route.user import ApiUserCreate
from sqlalchemy.future import select
from sqlalchemy.orm import Session


class User:

    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def all(self):
        query = await self.db_session.execute(select(UserDb)
                                              .order_by(UserDb.updated_at))
        return query.scalars().all()

    async def get(self, user_id: int):
        return self.db_session.execute(select(UserDb).where(UserDb.id == user_id))

    async def create(self, user: ApiUserCreate) -> None:
        new_user = UserDb(name=user.name, email=user.email,
                          memo=user.memo, image=user.image)
        self.db_session.add(new_user)
        await self.db_session.flush()
