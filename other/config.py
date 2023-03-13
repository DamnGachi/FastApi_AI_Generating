import os

from dotenv import load_dotenv
from envparse import Env

load_dotenv()
env = Env()
SENDER_MAIL = os.environ.get("SENDER_MAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")
RECIPIENT_MAIL = os.environ.get("RECIPIENT_MAIL")
redis_url = os.environ.get("REDIS_URL")
openai_secret_key = os.environ.get("SECRET_OPENAI")
