import requests
import allure
from endpoints.endpoint import Endpoint


class UpdatePost(Endpoint):
    @allure.step('Update a post')
    def make_changes_in_post(self, obj_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{obj_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response



