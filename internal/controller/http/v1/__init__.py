from internal.config.base_conf import fastapi_users
from fastapi import APIRouter
from internal.config.base_conf import auth_backend
from internal.dto.auth import UserCreate, UserRead
from . import applications, auth, health, ai_generate

router = APIRouter()
router.include_router(
    applications.router,
    prefix="/applications",
    tags=["applications"],
)
router.include_router(
    health.router,
    prefix="/health",
    tags=["health"],
)
router.include_router(
    ai_generate.router,
    prefix="/AI",
    tags=["AI"],
)
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)
