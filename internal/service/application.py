import datetime
import uuid
from typing import Sequence

import sqlalchemy as sa
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

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
        query = (
            self.session.query(Application)
            .filter(Application.deleted_at.is_(None))
            .filter(Application.phone.contains(dto.phone))
            .filter(Application.email.contains(dto.email))
        )
        return await query.all()

    async def find_one_or_fail(self, application_id: uuid.UUID) -> Application:
        application = (
            self.session.query(Application)
            .filter(Application.deleted_at.is_(None))
            .filter_by(id=application_id)
            .one_or_none()
        )
        if application is None:
            raise HTTPException(status_code=404, detail="Application not found")
        return application

    async def delete(self, application_id: uuid.UUID) -> Application:
        application = await self.find_one_or_fail(application_id)
        application.deleted_at = datetime.utcnow()
        await self.session.commit()
        return application
