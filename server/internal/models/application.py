# import sqlalchemy as sa
from sqlalchemy import Column, String, Text, UniqueConstraint
from internal.models.base import Base


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
