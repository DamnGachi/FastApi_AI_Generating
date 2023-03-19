import asyncio
import aioredis
from celery import Celery
from fastapi import BackgroundTasks, FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from internal.config.database import create_database
from pkg.rabbitmq.rpc import RPCClient, RPCServer


def start_redis_cache():
    async def wrapper():
        # background_tasks = BackgroundTasks()
        redis = aioredis.from_url(
            "redis://localhost", encoding="utf8", decode_responses=True
        )
        FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

    return wrapper


def startup_database(url: str):
    async def wrapper():
        await create_database(url)

    return wrapper


def startup_rpc_server(rpc: RPCServer):
    async def wrapper():
        loop = asyncio.get_event_loop()
        rpc.set_event_loop(loop)
        asyncio.ensure_future(rpc.connect())

    return wrapper


def startup_rpc_client(rpc: RPCClient):
    async def wrapper():
        loop = asyncio.get_event_loop()
        rpc.set_event_loop(loop)
        rpc.state.rpc = await rpc.connect(
            durable=True,
            auto_delete=True,
        )

    return wrapper


def shutdown_rpc_client(rpc: RPCClient):
    async def wrapper():
        await rpc.state.rpc.close()

    return wrapper
