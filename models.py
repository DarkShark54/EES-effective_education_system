import psycopg2
from psycopg2 import Error

class Datebase:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.datebase = database
        self.connection = None
        self.cursor = None

    def connection_to_base(self):
        try:
            # Подключение к существующей базе данных
            self.connection = psycopg2.connect(user=self.user, password=self.password, host=self.host, port=self.port,
                                               database=self.datebase)
            self.cursor = self.connection.cursor()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    def close_to_base(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Соединение с PostgreSQL закрыто")

    def get_request(self, text_request):
        self.cursor.execute(text_request)
        record = self.cursor.fetchall()
        return record

    def post_request(self, text_request):
        self.cursor.execute(text_request)
        self.connection.commit()

    def put_request(self, text_request):
        self.cursor.execute(text_request)
        self.connection.commit()

    def delete_request(self, text_request):
        self.cursor.execute(text_request)
        self.connection.commit()


date_base = Datebase("postgres", "nioklCH545565", "127.0.0.1", "5432", "EES")
