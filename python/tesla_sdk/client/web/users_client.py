from client.web.base_web_client import BaseWebClient

class UsersClient(BaseWebClient):

    def backup_key(self):
        return self.httpGet(
            "/api/1/users/backup_key"
        )

    def feature_config(self):
        return self.httpGet(
            "/api/1/users/feature_config"
        )

    def me(self):
        return self.httpGet(
            "/api/1/users/me"
        )
    
    def orders(self):
        return self.httpGet(
            "/api/1/users/orders"
        )
    
    def region(self):
        return self.httpGet(
            "/api/1/users/region"
        )