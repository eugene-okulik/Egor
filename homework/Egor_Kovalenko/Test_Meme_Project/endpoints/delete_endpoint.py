from endpoints.endpoint import Endpoint
import requests
import allure


class MemeDelete(Endpoint):

    @allure.step('Delete mem dy id')
    def delete_mem(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(f"{self.url}/meme/{meme_id}", headers=headers)
        return self.response
