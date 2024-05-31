import requests
import allure
from endpoints.endpoint import Endpoint
from src.enum.global_enums import GlobalErrorMessages


class GetPost(Endpoint):
    length = None

    @allure.step('Get all posts')
    def get_all_posts(self):
        """ Метод получения всех постов"""
        self.response = requests.get(self.url, headers=None)
        return self.response.json()

    @allure.step('Getting length of response')
    def get_length(self):
        self.response = requests.get(self.url, headers=None).json()
        self.length = len(self.response)
        return self.length

    @allure.step('Check length of response')
    def check_length_of_response(self, length):
        assert self.length == length, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

    @allure.step('Get a single post id')
    def get_single_post_id(self, obj_id, headers=None):
        self.response = requests.get(
            f'{self.url}/{obj_id}',
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Check that id is equal to expected')
    def check_response_id_is_correct(self, obj_id):
        assert self.json['id'] == obj_id
