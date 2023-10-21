
from client.base_client import BaseClient
import requests


class BaseWebClient(BaseClient):

    def __init__(
        self,
        auth_token,
        base_url="https://fleet-api.prd.na.vn.cloud.tesla.com"
    ):
        self.base_url = base_url

        super().__init__(auth_token)

    def httpGet(self, path, params=None, **kwargs):
        return requests.get(
            self.base_url + path,
            params=params,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer " + self.auth_token
            },
            **kwargs
        )

    def httpPost(self, path, data=None, json=None, **kwargs):
        return requests.post(
            self.base_url + path,
            data=data,
            json=json,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer " + self.auth_token
            }
            ** kwargs
        )
