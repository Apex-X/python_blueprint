from pydantic import BaseModel
from yaml.loader import SafeLoader
from colorama import Fore
import yaml
import json


class App(BaseModel):
    migrations_path: str


class HTTP(BaseModel):
    host: str
    port: int
    workers: int
    debug: bool


# @apex:database:tag
class Database(BaseModel):
    host: str
    port: int
    user: str
    password: str
    db_name: str
# @apex:end


# @apex:redis:tag
class Redis(BaseModel):
    host: str
    port: int
    password: str
    db: int
# @apex:end


class Config(BaseModel):
    log_level: str
    locale_path: str
    app: App
    http: HTTP
    # @apex:database:tag
    database: Database
    # @apex:end
    # @apex:redis:tag
    redis: Redis
    # @apex:end


cfg: Config = None


def load_config(config_path: str) -> None:
    with open(config_path) as f:
        config = yaml.load(f, Loader=SafeLoader)
        global cfg
        cfg = Config(**config)

    print(Fore.YELLOW + "+----------------------------------------------+")
    print(Fore.BLUE + "|                 Config Loaded                |")
    print(Fore.YELLOW + "+----------------------------------------------+")
    print(Fore.GREEN + json.dumps(cfg.model_dump(), indent=4))
    print(Fore.YELLOW + "+----------------------------------------------+")


def config() -> Config:
    """
    Get the configuration object
    :return: configuration object
    """
    global cfg
    return cfg
