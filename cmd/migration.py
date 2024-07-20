from config import cfg, load_config
from log import init_logger
from application.database import Database
from loguru import logger
import os
import glob


def __create_database(csr):
    try:
        csr.execute(
            f"CREATE DATABASE IF NOT EXISTS {cfg.database.db_name} DEFAULT CHARACTER SET 'utf8-mb4'",
        )
    except Exception as err:
        raise Exception('Failed creating database') from err


def migrate(config: str):
    """
    Migrate all migration files.\n

    e.g: python3 main.py migrate [config_path]\n
    """

    load_config(config)
    init_logger()

    try:
        connection = Database()
    except Exception as err:
        logger.fatal('Error while connecting to database: %s', err)

    cursor = connection.cursor()

    # create database if not exists
    try:
        cursor.execute(f'USE {cfg.database.db_name}')
        connection.commit()
    except Exception as err:
        logger.info(f'Database {cfg.database.db_name} does not exists.', err)
        __create_database(cursor)
        cursor.execute(f'USE {cfg.database.db_name}')
        logger.info(f'Database {cfg.database.db_name} created successfully.')
        connection.database = cfg.database.db_name

    # create tables
    logger.info('Migrating...')

    os.chdir(cfg.app.migrations_path)
    for file in glob.glob('*.up.sql'):
        print(f'Running migration {file}')
        with open(file) as f:
            try:
                cursor.execute(f.read())
                connection.commit()
            except Exception as e:
                logger.error(e)

    logger.info('Migration finished successfully')
