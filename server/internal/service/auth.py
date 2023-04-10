from fastapi import Depends
from internal.models.user import OAuthAccount, User
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_users.db import SQLAlchemyUserDatabase
from internal.config.database import get_session
from fastapi_users.models import UD, BaseOAuthAccount


class AuthService(object):
    def __init__(
        self,
        session: AsyncSession = Depends(get_session),
    ) -> None:
        self.session = session

    async def get_user_db(self):
        yield SQLAlchemyUserDatabase(self.session, User, OAuthAccount)

    async def create_user(self, user: UD) -> User:
        db_user = User(**user.dict())
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user

    async def get_user_by_email(self, email: str) -> User:
        return self.session.query(User).filter(User.email == email).first()

    async def create_oauth_account(
        self, oauth_account: BaseOAuthAccount[OAuthAccount, User]
    ) -> OAuthAccount:
        db_oauth_account = OAuthAccount(**oauth_account.dict())
        self.session.add(db_oauth_account)
        self.session.commit()
        self.session.refresh(db_oauth_account)
        return db_oauth_account

    async def get_oauth_account(self, provider: str, provider_id: str) -> OAuthAccount:
        return (
            self.session.query(OAuthAccount)
            .filter(
                OAuthAccount.provider == provider,
                OAuthAccount.provider_id == provider_id,
            )
            .first()
        )
