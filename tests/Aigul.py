# библиотека для работы с api
import pytest
import requests
from pprint import pprint

BASE_URL = 'https://restful-booker.herokuapp.com/booking'
AUTH_URL = 'https://restful-booker.herokuapp.com/auth'
STATUS_OK = 200

# запросить все записи и проверить что статус код 200
def test_get_all_bookings():
# запросить все записи и
    response = requests.get(BASE_URL)
# Проверить что статус код 200
    assert response.status_code == STATUS_OK
# распечатать ответ в виде джейсон файла
#     pprint(response.json())

    print(f'\n всего записей  {len(response.json())}')
# Проверка что записей определенное кол-во
    assert len(response.json()) > 39

# heders
    pprint(f' \n {response.headers}')
# проверка что в Хедерах содержится ключь 'Server'
    assert 'Server' in response.headers, 'There is no expected key'

def test_get_booking_with_id():
    response = requests.get(f'{BASE_URL}/1')
    response_data = response.json()
# ППП Проверка что  в ответе присутствуют все ключи. Создадим список ключей
    expected_keys = ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates']
    for key in expected_keys:
        assert key in response_data.keys()

# def test_get_booking_key_item():
#     response = requests.get(f'{BASE_URL}/1')
#     response_data = response.json()
#     assert response_data['firstname'] == 'Sally'
#     pprint(response.json())

# Используем метод post хотим создать новое бронирование
# надо создать переменную в которой будет хранится json.  bookingid': 493

def test_create_booking():
    pay_load = {
    "firstname" : "Jonatan",
    "lastname" : "Browny",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin": "2022-01-01",
        "checkout": "2022-09-01"
    },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(BASE_URL, json=pay_load)
    print(response.json())
    assert response.status_code == STATUS_OK
# проверка на то что этот пользователь сохранен на сервере
# сохраинть значение ключа bookingid' в переменную id
    id = response.json()['bookingid']
# получаем пользователя по id
    get_response = requests.get(f'{BASE_URL}/{id}')
    # проверяем что 'firstname' = Jonatan
    assert get_response.json()['firstname'] == 'Jonatan'

@pytest.fixture(scope='function') # фикстура создает пользовател и возвращает его id
def booking_id():
    payload = {
        "firstname": "Jolya",
        "lastname": "Browny",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2022-01-01",
            "checkout": "2022-09-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(BASE_URL, json=payload)
    booking_id = response.json()['bookingid']
    yield booking_id


# def test_create_booking_with_fixture(booking_id):
#     get_response = requests.get(f'{BASE_URL}/{booking_id}')
#     # проверяем что 'firstname' = Jonatan
#     assert get_response.json()['firstname'] == 'Jo'


@pytest.fixture(scope='function') # фикстура авторизует пользователя и возвращает токен, он нужен чтобы use метод delete
def token():
     payload = {
        'username': 'admin',
        'password': 'password123'
                }
     response = requests.post(AUTH_URL, json=payload)
     booking_token = response.json()['token']
     assert response.status_code == STATUS_OK
     yield booking_token

def test_create_auth_with_fixture(token):
    get_response = requests.get(f'{BASE_URL}/{token}')
    print((f'{BASE_URL}/{token}'))

# Создадим метод DELETE для этого надо сформировать запрос в котором указать id и в heders указать token см ТЗ на сайте
def test_delete_new_booking(booking_id, token):
    headers = {'Cookie': f'token={token}'}
    response = requests.delete(f'{BASE_URL}/{booking_id}', headers=headers)
    assert response.status_code == 201
#     проверка того что запись удалена
    get_response = requests.get(f'{BASE_URL}/{booking_id}')
    assert get_response.status_code == 404

# Метод который позволяет валидировать структуру json в запросе
# см https://python-jsonschema.readthedocs.io/en/stable/
# from jsonschema import validate

