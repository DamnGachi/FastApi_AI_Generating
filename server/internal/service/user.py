from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from internal.db.models import User


# Query all users
async def get_users(db):
    stmt = select(User)
    result = await db.execute(stmt)
    return result.scalars().all()


# Query a specific user by ID
async def get_user(user_id, db: AsyncSession):
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    return result.scalars().first()
