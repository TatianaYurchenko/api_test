import requests
from pprint import pprint
from tests.Testing_2.data_url import *
from tests.Testing_2.test_data import support_message

STATUS_OK = 200
class TestListUsers:
    def test_get_list_users_response(self):
        url = f"""{BASE_URL}{GET_LIST_USERS}2"""    # ЭТО ВЫНЕСТИ В ПЕРЕМЕННЫЕ КЛАССА
        response = requests.get(url)                #  СДЕЛАТЬ ОТДЕЛЬНО МЕТИОДЫ GET PUT POST И Т.П.
        assert response.status_code == STATUS_OK
        # print(response)
    # можем вытащить из ответа текст, json или какой то параметр в json
    #     pprint(response.text)
        pprint(response.json())
        pprint(response.json()["data"][0]['email'])

# Проверка что номерация страницы совпадает с заявленной Так же можно проверить кол-во элементов на странице
# 'per_page': 6
    def test_get_status_code(self):
        url = f"""{BASE_URL}{GET_LIST_USERS}2"""
        response = requests.get(url)
        assert response.json()["page"] == 2

#  'support': {'text': 'To keep ReqRes free, contributions towards server costs '
#                      'are appreciated!',
#              'url': 'https://reqres.in/#support-heading'},

    def test_get_support_message(self):
        url = f"""{BASE_URL}{GET_LIST_USERS}2"""
        response = requests.get(url)
        support_key = response.json()["support"]
        message = support_key["text"]
        assert message == support_message, 'не равны'

class Test_Single_User:
    def test_get_response(self):
        url = f"""{BASE_URL}{SINGLE_USER}/2"""
        response = requests.get(url)
        data = response.json()["data"]
        get_id = data['id']
        assert get_id == 2

    def test_get_status_code_200(self):
        url = f"""{BASE_URL}{SINGLE_USER}/2"""
        response = requests.get(url)
        assert response.status_code == 200

    def test_get_status_code_404(self):
        url = f"""{BASE_URL}{SINGLE_USER}/23"""
        response = requests.get(url)
        assert response.status_code == 404

    def test_get_emoty_response(self):
        url = f"""{BASE_URL}{SINGLE_USER}/23"""
        response = requests.get(url, )
        assert response.text == '{}'

class TestPostCreate: # можно сделать проверки на то что входные данные передаются чачтично. ТЕ только "name
    data = {
            "name": "morpheus",
            "job": "leader"
    }

    def test_create_post(self):
        url = f"""{BASE_URL}{SINGLE_USER}"""
        response = requests.post(url, data=self.data)
        print(response.json())

    def test_get_status_code_201(self):
        url = f"""{BASE_URL}{SINGLE_USER}"""
        response = requests.post(url, data=self.data)
        assert response.status_code == 201

class TestPutCreate:
    data = {
            "name": "morpheus",
            "job": "leader"
    }
    data_put = {
        "name": "morpheus",
        "job": "zion resident"
    }
    def test_create_and_update(self):
        url = f"""{BASE_URL}{SINGLE_USER}"""
        put_url = f"""{BASE_URL}{SINGLE_USER}/2"""
        response1 = requests.post(url, data=self.data)
        print(response1.json())
        response2 = requests.put(put_url, data=self.data_put)
        print(response2.json())

class TestDelateCreate:
    data = {
            "name": "morpheus",
            "job": "leader"

    }
    def test_create_and_update(self):
        url = f"""{BASE_URL}{SINGLE_USER}"""
        put_url = f"""{BASE_URL}{SINGLE_USER}/2"""
        response1 = requests.post(url, data=self.data)
        print(response1.json())
        response2 = requests.delete(put_url)
        print(response2.json())