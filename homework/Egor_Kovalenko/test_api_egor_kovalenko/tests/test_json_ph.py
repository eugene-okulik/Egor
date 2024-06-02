import pytest

TEST_VALID_DATA = [
    {
        "name": "HOME-PC",
        "data": {
            "year": 2024,
            "price": 1500,
            "CPU model": " Intel Xeon E5 2650 v2 OEM ",
            "Hard disk size": "1 TB"
        }
    }
]

TEST_INVALID_DATA = [
    {
        "name": "ХОУМ-ПС",
        "data": {
            "year": 2023,
            "price": 1600,
            "CPU model": " Intel Xeon E5 2650 v2 OEM ",
            "Hard disk size": "2 TB"
        }
    },
    {
        "name": "#$^^&*)_!",
        "data": {
            "year": 2023,
            "price": 1600,
            "CPU model": " Intel Xeon E5 2650 v2 OEM ",
            "Hard disk size": "2 TB"
        }
    }
]


@pytest.mark.smoke('smoke test')
@pytest.mark.parametrize('data', TEST_VALID_DATA)
def test_add_a_post(create_post_endpoint, data):
    create_post_endpoint.create_new_post(payload=data)
    create_post_endpoint.assert_response_is_200()
    create_post_endpoint.check_response_name_is_correct(data['name'])


@pytest.mark.smoke('smoke test')
@pytest.mark.parametrize('data', TEST_INVALID_DATA)
def test_create_post_with_invalid_datas(create_post_endpoint, data):
    create_post_endpoint.create_new_post(payload=data)
    create_post_endpoint.check_response_name_is_correct(data.get('name'))
    # create_post_endpoint.assert_response_is_400()


def test_put_a_post(update_post_endpoint, post_id):
    payload = {
        "name": "HOME-PC-12",
        "data": {
            "year": 2021,
            "price": 1610,
            "CPU model": " Intel Xeon E5 2650 v2 12OEM ",
            "Hard disk size": "21 TB",
        }
    }
    update_post_endpoint.make_changes_in_post(post_id, payload)
    update_post_endpoint.check_response_name_is_correct(payload.get('name'))
    update_post_endpoint.assert_response_is_200()


def test_patch_a_post(patch_post_endpoint, post_id):
    payload = {
        "name": "HOME-PC_1",
        "data": {
            "year": 2023
        }
    }
    patch_post_endpoint.partially_update_post(post_id, payload)
    patch_post_endpoint.check_response_name_is_correct(payload.get('name'))
    patch_post_endpoint.assert_response_is_200()


def test_get_all_posts(get_post_endpoint):
    get_post_endpoint.get_all_posts()
    get_post_endpoint.assert_response_is_200()


def test_check_length_posts(get_post_endpoint, length_post):
    get_post_endpoint.get_length()
    get_post_endpoint.check_length_of_response(length_post)
    # get_post_endpoint.assert_response_is_200()


@pytest.mark.smoke('smoke test')
def test_get_single_post(get_post_endpoint, post_id):
    get_post_endpoint.get_single_post_id(post_id)
    get_post_endpoint.assert_response_is_200()
    get_post_endpoint.check_response_id_is_correct(post_id)


@pytest.mark.smoke('smoke')
def test_delete_posts(delete_post_endpoint, post_id):
    delete_post_endpoint.delete_post(post_id)
    delete_post_endpoint.assert_response_is_200()
