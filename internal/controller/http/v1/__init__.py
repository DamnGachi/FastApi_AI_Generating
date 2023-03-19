from fastapi import APIRouter

from . import applications, health, ai_generate

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
