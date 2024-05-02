import requests


def add_a_post():
    body = {
        "name": "HOME-PC",
        "data": {
            "year": 2024,
            "price": 1500,
            "CPU model": " Intel Xeon E5 2650 v2 OEM ",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=body)
    assert response.status_code == 200, 'Status code is incorrect'


def get_a_new_post_id():
    body = {
        "name": "HOME-PC",
        "data": {
            "year": 2024,
            "price": 1500,
            "CPU model": " Intel Xeon E5 2650 v2 OEM ",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=body)
    return response.json()['id']


def get_single_post():
    post_id = get_a_new_post_id()
    response = requests.get(f'https://api.restful-api.dev/objects{post_id}').json()
    assert response['id'] == post_id


def clear_post_id(post_id):
    response = requests.delete(f'https://api.restful-api.dev/objects{post_id}')


def update_post():
    post_id = get_a_new_post_id()
    body = {
        "name": "HOME-PC_EGOR",
        "data": {
            "year": 2024,
            "price": 1500,
            "CPU model": " Intel Xeon E5 2650 v2 OEM ",
            "Hard disk size": "2 TB"
        }
    }
    response = requests.put(f'https://api.restful-api.dev/objects{post_id}', json=body)
    assert response.json()['name'] == 'HOME-PC_EGOR'
    clear_post_id(post_id)


def partially_update_post():
    post_id = get_a_new_post_id()
    body = {
        "name": "HOME-PC",
        "data": {
            "year": 2023
        }
    }
    response = requests.patch(f'https://api.restful-api.dev/objects{post_id}', json=body).json()
    clear_post_id(post_id)


def delete_object():
    post_id = get_a_new_post_id()
    response = requests.delete(f'https://api.restful-api.dev/objects{post_id}').json()


add_a_post()
