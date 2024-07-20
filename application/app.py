from typing import Optional
from .database import Database
from config import cfg
import redis


class Application:
    db: Database = None
    redis_client = None

    def __init__(self):
        self.db = Database()
        self.redis_client = redis.Redis(
            host=cfg.redis.host,
            port=cfg.redis.port,
            password=cfg.redis.password,
            db=cfg.redis.db,
        )


app: Optional[Application] = None


def load_app() -> None:
    global app
    app = Application()
