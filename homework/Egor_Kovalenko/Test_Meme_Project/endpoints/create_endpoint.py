from endpoints.endpoint import Endpoint
import requests
import allure


class CreateToken(Endpoint):
    @allure.step('Create a new token')
    def create_token(self, body, headers=None):
        """Авторизация"""
        self.response = requests.post(
            f'{self.url}/authorize',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        self.token = self.json['token']
        return self.response
