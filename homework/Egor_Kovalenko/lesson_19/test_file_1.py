import requests
import pytest
from enums import GlobalErrors

BASE_URL = 'https://api.restful-api.dev'


@pytest.fixture(scope='session')
def print_words_before_and_after_tests():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture()
def print_words_before_tests():
    print('before test')
    yield
    print('after tests')


@pytest.fixture()
def get_a_new_post_id():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        url=f'{BASE_URL}/objects',
        json=body,
        headers=headers
    )
    obj_id = response.json()['id']
    yield obj_id
    requests.delete(f'{BASE_URL}/objects/{obj_id}')


@pytest.mark.medium
def test_get_single_post(get_a_new_post_id, print_words_before_and_after_tests):
    """Тест проверки, что полученный id, равен id созданного объекта"""
    response = requests.get(f'{BASE_URL}/objects/{get_a_new_post_id}')
    assert response.json()['id'] == get_a_new_post_id


@pytest.mark.medium
def test_get_all_posts(print_words_before_tests):
    response = requests.get(f'{BASE_URL}/objects').json()
    length_posts = len(response)
    assert len(response) == length_posts


@pytest.mark.critical
def test_partially_update_post(get_a_new_post_id, print_words_before_tests):
    body = {
        "name": "HOME-PC_1",
        "data": {
            "year": 2023
        }
    }
    response = requests.patch(f'{BASE_URL}/objects/{get_a_new_post_id}', json=body)
    assert response.json()['name'] == "HOME-PC_1"


@pytest.mark.parametrize('input_param', [
    ({
        "name": "ХОУМ-ПС",
        "data": {
            "year": 2024,
            "price": 1500,
            "CPU model": " Intel Xeon E5 2650 v2 OEM ",
            "Hard disk size": "1 TB"
        }
    }),
    ({
        "data": {
            "year": 2023,
            "price": 1600,
            "CPU model": " Intel Xeon E5 2650 v2 OEM ",
            "Hard disk size": "2 TB"
        }
    }),
    ({

    })
])
def test_create_new_posts(print_words_before_tests, input_param):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        url=f'{BASE_URL}/objects/',
        json=input_param,
        headers=headers
    )
    assert response.status_code == 200, GlobalErrors.WRONG_STATUS_CODE.value


@pytest.mark.critical
def test_delete_post(get_a_new_post_id, print_words_before_tests):
    response = requests.delete(f'{BASE_URL}/objects/{get_a_new_post_id}')
    assert response.status_code == 200, GlobalErrors.WRONG_STATUS_CODE.value
    response = requests.get(f'{BASE_URL}/objects/{get_a_new_post_id}')
    assert response.status_code == 404, GlobalErrors.WRONG_STATUS_CODE.value
