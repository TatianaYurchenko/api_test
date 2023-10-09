import requests
from pprint import pprint
from tests.test_tatiana.test_users.data_url_users import *

STATUS_OK = 200
NOT_FOUND = 404

class Test_users_get:
    data = {
        "id": 1212,
        "username": "Garry1",
        "firstName": "Garry",
        "lastName": "Kallahan",
        "email": "lo@mail.se",
        "password": "123",
        "phone": "123",
        "userStatus": 0
    }

    def test_create_users(self):
        # url = f'{BASE_URL}{CREATE_USERS}'
        url = "https://petstore.swagger.io/v2/user/createWithArray"
        response = requests.post(url, data=self.data)
        print(response.status_code)

    def test_get_users_by_username(self):
        url = f'{BASE_URL}{GET_USER_BY_USERNAME}Garry4'
        print(url)

        response = requests.get(url)
        # response = requests.post(url, data=self.data)
        print(response.json())
