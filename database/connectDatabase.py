import mysql.connector
from mysql.connector import pooling
import json


class Database:
    def __init__(self):
        with open("config.json", "r") as c:
            self.config = json.load(c)
            self.host = self.config["mariadb"]["host"]
            self.user = self.config["mariadb"]["user"]
            self.password = self.config["mariadb"]["password"]
            self.database = self.config["mariadb"]["database"]

    def check(self):
        state_database: bool = False
        connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )
        cursor = connection.cursor(prepared=True)
        cursor.execute("Show databases")
        tables = cursor.fetchall()

        for table in tables:
            if str(table[0]).lower() == "nyria":
                state_database = True
                print("Database faultless")

        if not state_database:
            self.create()

    def create(self):
        # create database
        pass

    async def connect(self, pool_name: str, pool_size: int):
        connection_pool: pooling.MySQLConnectionPool = pooling.MySQLConnectionPool(
            pool_size=pool_size,
            pool_name=pool_name,
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return connection_pool
