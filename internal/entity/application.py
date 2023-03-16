import sqlalchemy as sa

from internal.entity import mixin
from internal.entity.base import Base
from internal.entity.mixin import TimestampMixin


class Application(Base):
    extend_existing = True

    __table_args__ = {"extend_existing": True}
    (
        sa.UniqueConstraint("phone"),
        sa.UniqueConstraint("email"),
    )

    phone = sa.Column(sa.String(255), index=True, nullable=False)
    email = sa.Column(sa.String(255), index=True, nullable=False)
    text = sa.Column(sa.Text, nullable=False)
