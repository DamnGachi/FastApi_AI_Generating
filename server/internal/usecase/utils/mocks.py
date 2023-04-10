from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from internal.config.database import get_session


async def get_user_db(session: AsyncSession = Depends(get_session)):
    from internal.models.user import User

    yield SQLAlchemyUserDatabase(session, User)
