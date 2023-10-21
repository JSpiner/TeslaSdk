from client.web.vehicles_client import VehiclesClient
from client.web.users_client import UsersClient


class WebClient:

    def __init__(self, auth_token) -> None:
        self.vehicles = VehiclesClient(auth_token)
        self.users = UsersClient(auth_token)
