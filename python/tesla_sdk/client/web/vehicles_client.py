from client.web.base_web_client import BaseWebClient


class VehiclesClient(BaseWebClient):

    def list(self, page, per_page):
        return self.httpGet(
            "/api/1/vehicles"
        )