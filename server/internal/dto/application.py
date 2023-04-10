import uuid
from dataclasses import dataclass

from fastapi import Query
from pydantic import BaseModel, EmailStr


class BaseApplication(BaseModel):

    text: str
    phone: str
    email: EmailStr


class ApplicationRead(BaseApplication):

    id: uuid.UUID

    class Config(object):
        orm_mode = True


@dataclass
class ApplicationFilter(object):

    phone: str = Query("")
    email: str = Query("")
