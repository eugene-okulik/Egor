import allure
import requests
from src.enum.global_enums import GlobalErrorMessages


class Endpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}
    post_id = None

    @allure.step('Check that name is equal to expected')
    def check_response_name_is_correct(self, name):
        """Проверка поля имени в ответе"""
        assert self.json['name'] == name, GlobalErrorMessages.WRONG_NAME.value

    @allure.step('Create a post')
    def create_new_post(self, payload, headers=None):
        """Создание нового обьекта"""
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.post_id = self.json['id']
        return self.response

    @allure.step('Check that response is 200')
    def assert_response_is_200(self):
        """ Проверка статус-код 200"""
        assert self.response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value

    @allure.step('Check that title is the same as sent')
    def assert_response_is_400(self):
        """ Проверка статус-код 400"""
        assert self.response.status_code == 400, GlobalErrorMessages.WRONG_STATUS_CODE.value



