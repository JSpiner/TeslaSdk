from tesla_sdk.client.web.vehicles_client import VehiclesClient
from tesla_sdk.client.web.users_client import UsersClient


class WebClient:

    def __init__(self, auth_token) -> None:
        self.vehicles = VehiclesClient(auth_token)
        self.users = UsersClient(auth_token)
