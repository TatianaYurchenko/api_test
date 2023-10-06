import pytest
import requests
from pprint import pprint
from data.urls import base_url # не нужно тк есть в my_requests
from data.data_files import StatusCompanies
from src.my_requests import MyRequests


class TestStatusCompanies:
    status_list = StatusCompanies.status_list
    request = MyRequests()
    @pytest.mark.parametrize("status", status_list)
    def test_get_active_companies(self, status):
        response = requests.get(f"""{base_url}/?status={status}&limit=1""") # {base_url} не нужно
        pprint(response.json())

    def test_get_closed_companies(self):
        response = requests.get(f"""{base_url}/?status=CLOSED""")
        # response = requests.get(base_url)
        pprint(response.json())
        assert response.status_code == 200, f'Status code is not 200, status code is {response.status_code}'
        # print(response.url)

