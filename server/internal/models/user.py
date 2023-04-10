from datetime import datetime

from typing import List
from fastapi_users.db import (
    SQLAlchemyBaseOAuthAccountTableUUID,
    SQLAlchemyBaseUserTableUUID,
)
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer, MetaData, String

from sqlalchemy.orm import Mapped, relationship

from internal.models.base import Base

from sqlalchemy import (
    JSON,
    TIMESTAMP,
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Table,
)

metadata = MetaData()


class OAuthAccount(SQLAlchemyBaseOAuthAccountTableUUID, Base):
    provider_id = Column(String, nullable=False)
    provider = Column(String, nullable=False)


role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(role.c.id))
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
    oauth_accounts: Mapped[List[OAuthAccount]] = relationship(
        "OAuthAccount", lazy="joined"
    )

    def to_dict(self):
        d = super().to_dict()
        d["oauth_accounts"] = [a.to_dict() for a in self.oauth_accounts]
        return d


class UserDB(SQLAlchemyBaseUserTable):
    access_token = Column(String)
    refresh_token = Column(String)
    expires_at = Column(Integer)
