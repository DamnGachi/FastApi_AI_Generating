# import sqlalchemy as sa
from sqlalchemy import Column, String, Text, UniqueConstraint
from internal.entity import mixin
from internal.entity.base import Base
from internal.entity.mixin import TimestampMixin


class Application(Base):
    extend_existing = True

    __table_args__ = {"extend_existing": True}
    (
        UniqueConstraint("phone"),
        UniqueConstraint("email"),
    )

    phone = Column(String(255), index=True, nullable=False)
    email = Column(String(255), index=True, nullable=False)
    text = Column(Text, nullable=False)
