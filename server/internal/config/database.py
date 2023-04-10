from typing import Any, AsyncContextManager, AsyncGenerator, Callable

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from internal.config import settings
from internal.models.base import Base
from internal.usecase.utils import get_session

AsyncSessionGenerator = AsyncGenerator[AsyncSession, None]


async def create_database(url: str) -> None:
    engine = create_async_engine(
        url,
        pool_pre_ping=True,
        future=True,
    )
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    await engine.dispose()


engine = create_async_engine(
    settings.DATABASE_URI,
    pool_pre_ping=True,
    future=True,
)
factory = async_sessionmaker(
    engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:  # noqa: WPS430, WPS442
    async with factory() as session:
        yield session


override_session = get_session()
context_session = get_session()
