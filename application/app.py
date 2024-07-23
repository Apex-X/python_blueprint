from typing import Optional
from .database import Database
from config import config
import redis


class Application:
    # @apex:database:tag
    db: Database = None
    # @apex:end
    # @apex:redis:tag
    redis_client = None
    # @apex:end

    def __init__(self):
        # @apex:database:tag
        self.db = Database()
        # @apex:end
        # @apex:redis:tag
        self.redis_client = redis.Redis(
            host=config().redis.host,
            port=config().redis.port,
            password=config().redis.password,
            db=config().redis.db,
        )
        # @apex:end


application: Optional[Application] = None


def load_app() -> None:
    global application
    application = Application()


def app() -> Application:
    global application
    return application
