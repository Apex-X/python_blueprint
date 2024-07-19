import mysql.connector
from mysql.connector import errorcode
from config import cfg
import logging


class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def __connect(self):
        try:
            self.cnx = mysql.connector.connect(
                host=cfg.database.host,
                port=cfg.database.port,
                user=cfg.database.user,
                password=cfg.database.password,
                database=cfg.database.db_name,
            )
            self.cnx.reconnect()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise Exception(
                    'Something is wrong with your user name or password'
                )
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise Exception('Database does not exist')
            else:
                raise Exception(
                    'Unknown error while connecting to database'
                ) from err

    def disconnect(self):
        self.cnx.close()

    def cursor(self):
        ping_try = 0
        while True:
            try:
                self.cnx.ping(reconnect=True, attempts=3, delay=1)
                break
            except mysql.connector.Error as err:
                logging.error("error in mysql connection", err)
                if ping_try > 5:
                    raise Exception("mysql connection error")
                self.__connect()
                ping_try += 1

        return self.ctx.cursor()
