from models import data_base
from requests import requests_list


def index(request_type, request_name, data=0):
    return requests_list[request_type][request_name](data_base, data)


test = index("GET", "data_client", 1)
print(test)
