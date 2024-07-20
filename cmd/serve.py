from typing_extensions import Annotated
from server import http_server
from application import load_app
from config import load_config, cfg
from log import init_logger
from loguru import logger
import uvicorn
import typer


def serve(
        config_path: Annotated[str, typer.Argument(help="Path to the configuration file")] = "config.yml"):
    """
    Start the server.\n
    :param config_path: Path to the configuration file.\n
    """
    load_config(config_path)
    print_config()
    init_logger()
    logger.info("init logger successfully")

    load_app()
    logger.info("load application successfully")

    logger.info("start server")
    uvicorn.run(
        http_server,
        host=cfg.http.host,
        port=cfg.http.port,
        log_level=cfg.http.log_level,
    )
    logger.info("server started successfully")
