from locust import task, HttpUser, tag
import random


class JsonPlaceHolder(HttpUser):
    user_id = None

    @tag('tag1')
    @task
    def creating_a_resource(self):
        data = {
            'title': 'Example title',
            'body': 'some text',
            'userId': 1
        }
        response = self.client.post(
            '/posts',
            headers={
                'Content-type': 'application/json; charset=UTF-8',
            },
            json=data
        )
        self.user_id = response.json().get('id')

    @tag('tag3')
    @task(3)
    def getting_all_resource(self):
        with self.client.get('/posts', catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Wrong status_code")

    @tag('tag1', 'tag2')
    @task(3)
    def getting_resource_id(self):
        self.client.get(
            f'/posts/{self.user_id}',
            headers=None
        )

    @tag('tag4')
    @task(4)
    def updating_resource(self):
        body = {
            'title': 'Example title with extras',
            'body': 'some new text',
            'userId': 1
        }
        self.client.put(
            f'/posts/{self.user_id}',
            headers={
                'Content-type': 'application/json; charset=UTF-8',
            },
            json=body
        )

    @tag('tag4', 'tag5')
    @task
    def patching_a_resource(self):
        body = {
            'title': 'No text',
        },
        self.client.patch(
            f'/posts/{self.user_id}',
            headers={
                'Content-type': 'application/json; charset=UTF-8',
            },
            json=body
        )

    def on_stop(self):
        self.client.delete(
            f'/posts/{self.user_id}',
            headers=None
        )
