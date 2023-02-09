import mysql.connector
from mysql.connector import pooling
from mysql.connector.errors import Error
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
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
        except Error:
            print("Database not reachable")
            exit()

        cursor = connection.cursor(prepared=True)
        cursor.execute("Show databases")
        tables = cursor.fetchall()

        for table in tables:
            if str(table[0]).lower() == "nyria":
                state_database = True
                print("Database faultless")
                connection.close()

        if not state_database:
            self.create(connection=connection)

    @staticmethod
    def create(connection):
        cursor = connection.cursor()

        # create database Nyria
        cursor.execute("CREATE DATABASE Nyria")
        cursor.execute("USE Nyria")

        cursor.execute("CREATE TABLE bug_reports (userId BIGINT NOT NULL, reports INT NOT NULL)")
        cursor.execute("CREATE TABLE cards (serverId BIGINT NOT NULL, channelId BIGINT NOT NULL, color TEXT NOT NULL, background TEXT NOT NULL)")
        connection.commit()
        connection.close()

    def connect(self, pool_name: str, pool_size: int):
        connection_pool = pooling.MySQLConnectionPool(
            pool_size=pool_size,
            pool_name=pool_name,
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return connection_pool
