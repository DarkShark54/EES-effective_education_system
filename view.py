from models import data_base
from requests import *


def index(request_type, request_name, data=0):
    requests_list[request_type][request_name](data)


def client_authorization(data):
    data_base.connection_to_base()
    text_request = """SELECT teacher.id as AUTORIZED
                    FROM teacher
                    WHERE teacher.fio = {fio} AND teacher.password = {password};""".format(fio=data[0], password=data[1])
    records = data_base.post_request(text_request)
    data_base.close_to_base()
    return records


def get_client_data(data):
    data_base.connection_to_base()
    text_request = """SELECT teaching_class.id_subject, subject.name AS name_subject, teaching_class.class
                    FROM teaching_class LEFT JOIN subject ON id_subject = subject.id
                    WHERE teaching_class.id_teacher = {teacher_id};""".format(teacher_id=data[0])
    records = data_base.post_request(text_request)
    data_base.close_to_base()
    return records
