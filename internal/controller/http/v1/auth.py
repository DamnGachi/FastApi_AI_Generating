# from fastapi import Depends
# from fastapi_users import routers as auth_routers
# from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
# from internal.config.base_conf import get_jwt_strategy
# from internal.dto.auth import UserCreate
# from internal.config.base_conf import fastapi_users, oauth2_scheme
# from internal.entity.auth import User
# from fastapi.security import OAuth2AuthorizationCodeRequestForm

# google_oauth_router = auth_routers.OAuthRouter(
#     google_oauth_client, auth_backend, SECRET, prefix="/auth/google"
# )


# @google_oauth_router.post("/users", response_model=User)
# async def create_user(user: UserCreate):
#     user_db = SQLAlchemyUserDatabase


# # Define auth route to handle OAuth2 authorization requests
# @google_oauth_router.get("/auth")
# async def auth(request: OAuth2AuthorizationCodeRequestForm = Depends()):
#     return await oauth2_scheme.authorize(request)

# # Define callback route to handle OAuth2 authorization code exchange


# @google_oauth_router.get("/callback")
# async def callback(request: OAuth2AuthorizationCodeRequestForm = Depends()):
#     user = await oauth2_scheme.get_user(request)
#     return await get_jwt_strategy().get_login_response(user, request)

# # Define protected route that requires authorization


# @google_oauth_router.get("/protected")
# async def protected(user: User = Depends(fastapi_users.get_current_active_user)):
#     return {"message": "This is a protected route"}
