from tesla_sdk.client.base_client import BaseClient
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
            params={k: v for k, v in params.items() if v is not None},
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer " + self.auth_token
            },
            **kwargs
        ).json()

    def httpPost(self, path, params=None, json=None, **kwargs):
        return requests.post(
            self.base_url + path,
            params={k: v for k, v in params.items() if v is not None},
            json=json,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer " + self.auth_token
            }
            ** kwargs
        ).json()
