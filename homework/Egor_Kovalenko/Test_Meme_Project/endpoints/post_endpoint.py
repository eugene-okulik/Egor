from endpoints.endpoint import Endpoint
import allure
import requests


class PostEndpoint(Endpoint):

    @allure.step('Create a new meme')
    def create_mem(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            url=f'{self.url}/meme',
            json=body,
            headers=headers
        )
        # print(self.response.text, self.response.status_code)
        # self.json = self.response.json()
        # self.meme_id = self.json['id']

        return self.response
