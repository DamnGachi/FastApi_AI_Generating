from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, exceptions, models, schemas

from internal.entity.auth import User
from sqlalchemy.ext.asyncio import AsyncSession
from ..usecase.utils.mocks import get_session


# class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
#     reset_password_token_secret = "xxxxx"
#     verification_token_secret = "xxxxx"

#     async def on_after_register(self, user: User, request: Optional[Request] = None):
#         print(f"User {user.id} has registered.")

#     async def create(
#         self,
#         user_create: schemas.UC,
#         safe: bool = False,
#         request: Optional[Request] = None,
#     ) -> models.UP:
#         await self.validate_password(user_create.password, user_create)

#         existing_user = await self.user_db.get_by_email(user_create.email)
#         if existing_user is not None:
#             raise exceptions.UserAlreadyExists()

#         user_dict = (
#             user_create.create_update_dict()
#             if safe
#             else user_create.create_update_dict_superuser()
#         )
#         password = user_dict.pop("password")
#         user_dict["hashed_password"] = self.password_helper.hash(password)
#         user_dict["role_id"] = 1

#         created_user = await self.user_db.create(user_dict)

#         await self.on_after_register(created_user, request)

#         return created_user
class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    def __init__(self, user_db: AsyncSession):
        self.user_db = user_db

    async def create(
        self,
        user_create: schemas.UC,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        async with self.user_db() as session:
            await self.validate_password(user_create.password, user_create)

            existing_user = await session.get_by_email(user_create.email)
            if existing_user is not None:
                raise exceptions.UserAlreadyExists()

            user_dict = (
                user_create.create_update_dict()
                if safe
                else user_create.create_update_dict_superuser()
            )
            password = user_dict.pop("password")
            user_dict["hashed_password"] = self.password_helper.hash(password)
            user_dict["role_id"] = 1

            created_user = models.UP(**user_dict)
            session.add(created_user)
            await session.commit()
            await session.refresh(created_user)

            await self.on_after_register(created_user, request)

            return created_user


async def get_user_manager(user_db=Depends(get_session)):
    yield UserManager(user_db)
