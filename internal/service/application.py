import datetime
import uuid
from typing import Sequence

import sqlalchemy as sa
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from internal.config.database import async_session

from internal.dto.application import (
    ApplicationFilter,
    BaseApplication,
)
from internal.entity.application import Application
from internal.usecase.utils import get_session


class ApplicationService(object):
    def __init__(
        self,
        session: AsyncSession = Depends(get_session),
    ) -> None:
        self.session = session

    async def create(self, dto: BaseApplication) -> Application:
        application = Application(**dto.dict())
        self.session.add(application)
        await self.session.commit()
        return application

    async def find(self, dto: ApplicationFilter) -> Sequence[Application]:
        stmt = sa.select(Application).filter(
            sa.and_(
                Application.phone.contains(dto.phone),
                Application.email.contains(dto.email),
            )
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def find_one_or_fail(self, application_id: uuid.UUID) -> Application:
        stmt = sa.select(Application).filter(Application.id == application_id)
        result = await self.session.execute(stmt)
        application = result.scalar_one_or_none()
        if application is None:
            raise HTTPException(status_code=404, detail="Application not found")
        return application

    async def delete(self, application_id: uuid.UUID) -> Application:
        application = await self.find_one_or_fail(application_id)
        application.delete()
        await self.session.commit()
        return application
