import json
from api.client import Client


class Api(Client):
    USERS = '/users'
    REGISTER = '/register'
    BASE_URL = 'https://reqres.in/api'

    def list_users(self):

        url = self.BASE_URL + self.USERS + '?page=2'
        return self.get(url)

    def single_user_not_found(self):

        url = self.BASE_URL + self.USERS + '/23'
        return self.get(url)

    def single_user(self):
        url = self.BASE_URL + self.USERS + '/2'
        return self.get(url)

    def create(self, name: str, job: str):
        url = self.BASE_URL + self.USERS
        payload = json.dumps({
            "name": F"{name}",
            "job": F"{job}"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        return self.post(url, headers, payload)

    def delete_user(self, id: int):
        url = self.BASE_URL + self.USERS + F"/{id}"
        return self.delete(url)

    def create_user(self, email: str, password: str):
        url = self.BASE_URL + self.REGISTER
        data = json.dumps({
            "email": f'{email}',
            "password": f"{password}"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        return self.post(url, headers, data)

    def create_user_error(self, email: str):
        url = self.BASE_URL + self.REGISTER
        data = json.dumps({
            "email": f'{email}'
        })
        headers = {
            'Content-Type': 'application/json'
        }
        return self.post(url, headers, data)


api = Api()
