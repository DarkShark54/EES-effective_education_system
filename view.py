from models import database
from requests import requests_list


def index(request_type, request_name, data=None):
    database.connection_to_base()
    final_record = requests_list[request_type][request_name](database, data)
    database.close_to_base()
    return final_record

def check_database_connection():
    if database is None:
        return "Ошибка подключения к базе данных!\n Пожалуйста проверте настройки и перезапустите программу."
    database.connection_to_base()
    if not database.check_connection_to_base():
        return "Ошибка подключения к базе данных!\n Пожалуйста проверте настройки и перезапустите программу."
    else:
        database.close_to_base()
        return "Подключение к базе данных успешно!"
