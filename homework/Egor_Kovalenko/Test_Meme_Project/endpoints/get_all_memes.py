from endpoints.endpoint import Endpoint
import allure
import requests


class GetAllMemes(Endpoint):

    @allure.step('Getting all memes list')
    def get_all_memes(self, headers=None):
        self.response = requests.get(
            url=f'{self.url}/meme',
            headers=headers
        )
        self.json = self.response.json()
        return self.response
