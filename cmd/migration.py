from config import config, load_config
from log import init_logger
from application.database import Database
from loguru import logger
import os
import glob


def __create_database(csr):
    try:
        csr.execute(
            f"CREATE DATABASE IF NOT EXISTS {config().database.db_name} DEFAULT CHARACTER SET 'utf8-mb4'",
        )
    except Exception as err:
        raise Exception('Failed creating database') from err


def migrate(config_path: str):
    """
    Migrate all migration files.\n

    e.g: python3 main.py migrate [config_path]\n
    """

    load_config(config_path)
    init_logger()

    try:
        connection = Database()
    except Exception as err:
        logger.fatal('Error while connecting to database: %s', err)

    cursor = connection.cursor()

    # create database if not exists
    try:
        cursor.execute(f'USE {config().database.db_name}')
        connection.commit()
    except Exception as err:
        logger.info(f'Database {config().database.db_name} does not exists.', err)
        __create_database(cursor)
        cursor.execute(f'USE {config().database.db_name}')
        logger.info(f'Database {config().database.db_name} created successfully.')
        connection.database = config().database.db_name

    # create tables
    logger.info('Migrating...')

    os.chdir(config().app.migrations_path)
    for file in glob.glob('*.up.sql'):
        print(f'Running migration {file}')
        with open(file) as f:
            try:
                cursor.execute(f.read())
                connection.commit()
            except Exception as e:
                logger.error(e)

    logger.info('Migration finished successfully')
