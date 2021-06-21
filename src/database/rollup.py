from dbschema import engine, Base
import asyncio


async def rollup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(rollup())
