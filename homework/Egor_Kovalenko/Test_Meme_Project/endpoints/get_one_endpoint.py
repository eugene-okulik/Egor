from endpoints.endpoint import Endpoint
import allure
import requests


class GetOneMeme(Endpoint):

    @allure.step('Getting meme by ID')
    def get_one_meme(self, mem_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=f'{self.url}/meme/{mem_id}',
            headers=headers
        )
        self.json = self.response.json()
        self.meme_id = self.json['id']
        return self.response
