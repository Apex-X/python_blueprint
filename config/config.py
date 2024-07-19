from pydantic import BaseModel
from yaml.loader import SafeLoader
from colorama import Fore
import yaml
import json


class HTTP(BaseModel):
    host: str
    port: int
    workers: int
    debug: bool
    log_level: str


class Database(BaseModel):
    host: str
    port: int
    user: str
    password: str


class Redis(BaseModel):
    host: str
    port: int
    password: str
    db: int


class Config(BaseModel):
    log_level: str
    http: HTTP
    database: Database
    redis: Redis


cfg: Config = None


def load_config(config_path: str):
    with open(config_path) as f:
        config = yaml.load(f, Loader=SafeLoader)
        global cfg
        cfg = Config(**config)

    print(Fore.YELLOW + "+----------------------------------------------+")
    print(Fore.BLUE + "|                 Config Loaded                |")
    print(Fore.YELLOW + "+----------------------------------------------+")
    print(Fore.GREEN + json.dumps(cfg.model_dump()))
    print(Fore.YELLOW + "+----------------------------------------------+")
