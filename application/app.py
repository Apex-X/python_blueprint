from typing import Optional
from .database import Database
from config import config
import redis


class Application:
    db: Database = None
    redis_client = None

    def __init__(self):
        self.db = Database()
        self.redis_client = redis.Redis(
            host=config().redis.host,
            port=config().redis.port,
            password=config().redis.password,
            db=config().redis.db,
        )


application: Optional[Application] = None


def load_app() -> None:
    global application
    application = Application()


def app() -> Application:
    global application
    return application
