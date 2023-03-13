import json
import os

import pytest

from internal.app.app import create_app
from internal.entity.base import Base

os.environ["ENV"] = "test"

if os.getenv("ENV") not in ["test"]:
    msg = f"ENV is not test, it is {os.getenv('ENV')}"
    pytest.exit(msg)

from fastapi.testclient import TestClient
from loguru import logger
from sqlalchemy.ext.asyncio import create_async_engine

from internal.config import settings

# from app.core.container import Container
# from app.main import AppCreator
# from app.model.post import Post
# from app.model.user import User


def insert_default_data(conn):
    user_default_file = open("./tests/default_insert_data/users.json", "r")
    user_default_data = json.load(user_default_file)
    for user in user_default_data:
        conn.execute(
            User.__table__.insert(),
            {
                "email": user["email"],
                "password": user["password"],
                "user_token": user["user_token"],
                "name": user["name"],
                "is_active": user["is_active"],
                "is_superuser": user["is_superuser"],
            },
        )
    post_default_file = open("./tests/default_insert_data/posts.json", "r")
    post_default_data = json.load(post_default_file)
    for post in post_default_data:
        conn.execute(
            Post.__table__.insert(),
            {
                "title": post["title"],
                "content": post["content"],
                "user_token": post["user_token"],
                "is_published": post["is_published"],
            },
        )


def reset_db():
    engine = create_async_engine(settings.DATABASE_URI["test"])
    logger.info(engine)
    with engine.begin() as conn:
        Base.metadata.drop_all(conn)
        Base.metadata.create_all(conn)
        insert_default_data(conn)
    return engine


@pytest.fixture
def client():
    reset_db()
    app_creator = create_app()
    app = app_creator.app
    with TestClient(app) as client:
        yield client


@pytest.fixture
def container():
    return Container()
