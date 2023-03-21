from celery import Celery
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import api
from sqlalchemy.exc import DBAPIError, NoResultFound

from internal.config import database, events, settings
from internal.controller.amqp.router import rpc_router
from internal.controller.http.router import api_router
from internal.usecase.utils.exception_handlers import (
    database_error_handler,
    database_not_found_handler,
    http_exception_handler,
)
from pkg.rabbitmq.rpc.client import RPCClient
from pkg.rabbitmq.rpc.server import RPCServer
from httpx_oauth.clients.google import GoogleOAuth2


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.NAME,
        description=settings.DESCRIPTION,
        version=settings.VERSION,
        openapi_url="{0}/openapi.json".format(settings.DOCS),
        swagger_ui_parameters=settings.SWAGGER_UI_PARAMETERS,
    )
    celery_app = Celery("tasks")
    REDIS_URL = "redis://localhost:6379/0"

    celery_app.conf.broker_read_url = REDIS_URL
    celery_app.conf.result_backend = REDIS_URL

    server = RPCServer(settings.RABBITMQ_URI)
    client = RPCClient(settings.RABBITMQ_URI, app.state)

    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    api.add_pagination(app)
    app.include_router(api_router, prefix=settings.API)
    server.include_router(rpc_router, prefix=settings.RPC)
    app.dependency_overrides.setdefault(*database.override_session)

    app.add_exception_handler(DBAPIError, database_error_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(NoResultFound, database_not_found_handler)
    app.add_event_handler(settings.STARTUP, events.start_redis_cache())
    app.add_event_handler(settings.STARTUP, events.startup_rpc_server(server))
    app.add_event_handler(settings.STARTUP, events.startup_rpc_client(client))
    app.add_event_handler(settings.SHUTDOWN, events.shutdown_rpc_client(client))

    return app
