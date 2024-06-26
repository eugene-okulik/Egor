import pytest
from endpoints.create_endpoint import CreateToken
from endpoints.post_endpoint import PostEndpoint
from endpoints.get_all_memes import GetAllMemes
from endpoints.get_one_endpoint import GetOneMeme
from endpoints.put_endpoint import UpdatePosts
from endpoints.delete_endpoint import MemeDelete


@pytest.fixture()
def delete_post_endpoint():
    return MemeDelete()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePosts()


@pytest.fixture()
def get_one_endpoint():
    return GetOneMeme()


@pytest.fixture()
def get_all_mem_endpoint():
    return GetAllMemes()


@pytest.fixture()
def getting_authorize():
    return CreateToken()


@pytest.fixture()
def create_post_endpoint():
    return PostEndpoint()


@pytest.fixture()
def authorization_token(getting_authorize):
    body = {
        "name": "Ega"
    }
    getting_authorize.create_token(body=body)
    yield getting_authorize.token


@pytest.fixture()
def meme_id(create_post_endpoint, authorization_token):
    payload = {
        "text": "funny cat meme",
        "url": "https://s09.stc.yc.kpcdn.net/share/i/4/2235353/wr-750.webp",
        "tags": ["oputi", "niputy"],
        "info": {
            "cute": 1,
            "fun": 2
        }
    }
    create_post_endpoint.create_mem(body=payload, headers={'Authorization': f'{authorization_token}'})
    id_mem = create_post_endpoint.response.json()['id']
    yield id_mem
