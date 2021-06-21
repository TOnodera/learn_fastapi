from database.dbschema import async_session
from Domain.Repository.User import User


async def get_user():
    async with async_session() as session:
        async with session.begin():
            yield User(session)
