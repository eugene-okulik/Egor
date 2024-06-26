import allure
import requests
from src.enums.global_enums import GlobalErrorMessages


class Endpoint:
    url = 'http://167.172.172.115:52355'
    headers = {'Content-Type': 'application/json', 'Authorization': None}
    token = None
    response = None
    json = None
    meme_id = None

    @allure.step('Validate data')
    def validate_schema(self, schema):
        """Метод валидации ответа по схеме"""
        if isinstance(self.response.json(), list):
            for item in self.response.json():
                schema(item)
            else:
                schema(self.response.json())
            return self

    @allure.step('Check response code is 200')
    def check_response_200_code(self):
        assert self.response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value

    @allure.step('Check that id is equal to expected')
    def check_response_id_is_correct(self, meme_id):
        """ Проверка ID"""
        assert self.json['id'] == meme_id, GlobalErrorMessages.WRONG_ID.value

    @allure.step('Check response code is 400')
    def check_response_400_code(self):
        assert self.response.status_code == 400, GlobalErrorMessages.WRONG_STATUS_CODE.value
