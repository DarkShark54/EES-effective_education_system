import psycopg2
from psycopg2 import Error
import datetime


class Database:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.connection = None
        self.cursor = None

    def connection_to_base(self):
        try:
            # Подключение к существующей базе данных
            self.connection = psycopg2.connect(user=self.user, password=self.password, host=self.host, port=self.port,
                                               database=self.database)
            self.cursor = self.connection.cursor()
        except (Exception, Error) as error:
            with open("log.txt", 'a') as file_log:
                file_log.write(str(datetime.datetime.now()) + ": Error! Failed to connect to database.\n")
            print("Ошибка при работе с PostgreSQL", error)

    def check_connection_to_base(self):
        if self.connection is None or self.cursor is None:
            return False
        else:
            return True

    def close_to_base(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()

    def get_request(self, text_request):
        self.cursor.execute(text_request)
        record = self.cursor.fetchall()
        return record

    def post_request(self, text_request):
        self.cursor.execute(text_request)
        record = self.cursor.fetchall()
        return record

    def put_request(self, text_request):
        self.cursor.execute(text_request)
        self.connection.commit()

    def delete_request(self, text_request):
        self.cursor.execute(text_request)
        self.connection.commit()


config = {"user": None, "password": None, "host_ip": None, "port": None, "database_name": None}
file_config = open("config.txt")
try:
    for string in file_config.readlines()[1:]:
        if string.split('=')[0] in config.keys():
            config[string.split('=')[0]] = string.split('=')[1][:len(string.split('=')[1])-1]
    if None in config.values():
        with open("log.txt", 'a') as file_log:
            file_log.write(str(datetime.datetime.now()) + ": Error! The database settings file is not formed correctly.\n")
        database = None
    else:
        database = Database(config["user"], config["password"],
                            config["host_ip"], config["port"], config["database_name"])
except IndexError:
    with open("log.txt", 'a') as file_log:
        file_log.write(str(datetime.datetime.now()) + ": Error! The database settings file is not formed correctly.\n")
    database = None
finally:
    file_config.close()
