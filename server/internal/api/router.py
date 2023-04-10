from fastapi import APIRouter

from internal.api.endpoints import router

api_router = APIRouter()
api_router.include_router(router, prefix="/v1")
