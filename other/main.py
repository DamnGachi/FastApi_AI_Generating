import aioredis
from celery import Celery
from fastapi import FastAPI, BackgroundTasks
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
import config
from generate_image import ai_router

app = FastAPI()

celery_app = Celery('tasks')

REDIS_URL = config.redis_url
celery_app.conf.broker_read_url = REDIS_URL
celery_app.conf.result_backend = REDIS_URL


@app.on_event("startup")
async def startup_event():
    background_tasks = BackgroundTasks()
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


# set routes to the api instance
app.include_router(ai_router)
