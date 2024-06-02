import requests
import allure
from endpoints.endpoint import Endpoint


class DeletePosts(Endpoint):

    def delete_post(self, post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/{post_id}',
            headers=headers
        )
        self.json = self.response.json()
        return self.response
