import pytest
from endpoints.create_posts import CreatePost
from endpoints.update_posts import UpdatePost
from endpoints.get_posts import GetPost
from endpoints.part_update_posts import PartUpdatePost
from endpoints.delete_posts import DeletePosts


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()


@pytest.fixture()
def get_post_endpoint():
    return GetPost()


@pytest.fixture()
def patch_post_endpoint():
    return PartUpdatePost()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePosts()


@pytest.fixture()
def post_id(create_post_endpoint):
    payload = {
        "name": "HOME-PC",
        "data": {
            "year": 2023,
            "price": 1600,
            "CPU model": " Intel Xeon E5 2650 v2 OEM ",
            "Hard disk size": "2 TB",
        }
    }
    create_post_endpoint.create_new_post(payload=payload)
    yield create_post_endpoint.post_id


@pytest.fixture()
def length_post(get_post_endpoint):
    yield get_post_endpoint.get_length()
