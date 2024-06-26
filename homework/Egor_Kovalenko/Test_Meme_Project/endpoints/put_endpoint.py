import requests
import allure
from endpoints.endpoint import Endpoint


class UpdatePosts(Endpoint):
    @allure.step('Update Post')
    def put_update_post(self, mem_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            url=f'{self.url}/meme/{mem_id}',
            json=body,
            headers=headers,
        )
        self.json = self.response.json()
        self.meme_id = self.json['id']
        return self.response
