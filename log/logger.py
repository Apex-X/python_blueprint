from loguru import logger
from config import config
import json
import sys


def serialize(record):
    subset = {
        "time": record["time"]["repr"],
        "level": record["level"].name,
        "message": record["message"],
        "path": record["file"]["path"]+":"+str(record["line"]),
    }
    return json.dumps(subset)


def formatter(record):
    record["extra"]["serialized"] = serialize(record)
    return "{extra[serialized]}\n"


def init_logger() -> None:
    logger.remove(0)
    logger.add(sys.stderr, format=formatter, level=config().log_level.upper())
