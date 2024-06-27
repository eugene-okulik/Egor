import pytest
from src.pydantic_schemas.post import MemeData

VALID_BODY = [
    {
        "text": "funny cat meme",
        "url": "https://s09.stc.yc.kpcdn.net/share/i/4/2235353/wr-750.webp",
        "tags": ["oputi", "niputy"],
        "info": {
            "cute": 1,
            "fun": 2
        }
    }
]

INVALID_BODY = [
    {
        "text": 1234,
        "url": "https://s09.stc.yc.kpcdn.net/share/i/4/2235353/wr-750.webp",
        "tags": ["oputi", "niputy"],
        "info": {
            "cute": 1,
            "fun": 2
        }
    }
]

BODY_FOR_UPDATE = [
    {
        "id": int,
        "text": "cat mems",
        "url": "https://s09.stc.yc.kpcdn.net/share/i/4/2235353/wr-750.webp",
        "tags": ["cat", "cute"],
        "info": {
            "cute": 1,
            "fun": 2
        }
    }

]


@pytest.mark.smoke('Smoke Test')
@pytest.mark.parametrize('body', VALID_BODY)
def test_create_mem_with_valid_data(create_post_endpoint, body, authorization_token):
    create_post_endpoint.create_mem(body=body, headers={'Authorization': f'{authorization_token}'})
    create_post_endpoint.validate_schema(MemeData)
    create_post_endpoint.check_response_200_code()


@pytest.mark.smoke('Smoke Test')
@pytest.mark.parametrize('body', INVALID_BODY)
def test_create_mem_with_invalid_data(create_post_endpoint, body, authorization_token):
    create_post_endpoint.create_mem(body=body, headers={'Authorization': f'{authorization_token}'})
    create_post_endpoint.check_response_400_code()


@pytest.mark.smoke('Smoke Test')
def test_getting_all_memes(get_all_mem_endpoint, authorization_token):
    get_all_mem_endpoint.get_all_memes(headers={'Authorization': f'{authorization_token}'})
    get_all_mem_endpoint.validate_schema(MemeData)
    get_all_mem_endpoint.check_response_200_code()


@pytest.mark.smoke('Smoke Test')
def test_getting_meme_by_id(get_one_endpoint, meme_id, authorization_token):
    get_one_endpoint.get_one_meme(mem_id=meme_id, headers={'Authorization': f'{authorization_token}'})
    get_one_endpoint.validate_schema(MemeData)
    get_one_endpoint.check_response_id_is_correct(meme_id)
    get_one_endpoint.check_response_200_code()


@pytest.mark.parametrize('body', BODY_FOR_UPDATE)
def test_put_a_post(update_post_endpoint, body, meme_id, authorization_token):
    body['id'] = int(meme_id)
    update_post_endpoint.put_update_post(mem_id=meme_id, body=body, headers={'Authorization': f'{authorization_token}'})
    update_post_endpoint.check_response_200_code()
    update_post_endpoint.check_response_id_is_correct(update_post_endpoint.response.json()['id'])


@pytest.mark.smoke('Smoke Test')
def test_delete_mem_by_id(delete_post_endpoint, meme_id, authorization_token):
    delete_post_endpoint.delete_mem(meme_id, headers={'Authorization': f'{authorization_token}'})
    delete_post_endpoint.check_response_200_code()
