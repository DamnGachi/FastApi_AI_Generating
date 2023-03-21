from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)


from internal.dto.auth_manager import get_user_manager
from internal.entity.auth import User
from httpx_oauth.clients.google import GoogleOAuth2

cookie_transport = CookieTransport(cookie_name="bonds", cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret="xxxxx", lifetime_seconds=3600)


# Настройки Google OAuth2
oauth2_scheme = GoogleOAuth2(
    client_id="42683423809-js6evf69ea36budsv10dvt5d7vqa4dr6.apps.googleusercontent.com",
    client_secret="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",
    # scopes={"profile": "Access profile information", "email": "Access email information"},
)
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()
