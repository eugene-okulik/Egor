import requests
import allure
from endpoints.endpoint import Endpoint


class PartUpdatePost(Endpoint):

    @allure.step('Part update post')
    def partially_update_post(self, obj_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{obj_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
