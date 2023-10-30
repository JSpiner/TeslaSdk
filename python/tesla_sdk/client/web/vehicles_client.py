from client.web.base_web_client import BaseWebClient


class VehiclesClient(BaseWebClient):

    def list(self, page: None, per_page: None):
        return self.httpGet(
            f"/api/1/vehicles",
            params={"page": page, "per_page": per_page},
        )

    def mobile_enabled(self, id):
        return self.httpGet(
            f"/api/1/vehicles/{id}/mobile_enabled",
            params=None,
        )

    def nearby_charging_sites(self, id, count: None, radius: None, detail: None):
        return self.httpGet(
            f"/api/1/vehicles/{id}/nearby_charging_sites",
            params={"count": count, "radius": radius, "detail": detail},
        )

    def recent_alerts(self, id):
        return self.httpGet(
            f"/api/1/vehicles/{id}/recent_alerts",
            params=None,
        )

    def service_data(self, id):
        return self.httpGet(
            f"/api/1/vehicles/{id}/service_data",
            params=None,
        )

    def share_invites(self, vehicle_id):
        return self.httpGet(
            f"/api/1/vehicles/{vehicle_id}/invitations",
            params=None,
        )

    def share_invites_create(self, vehicle_id):
        return self.httpPost(
            f"/api/1/vehicles/{vehicle_id}/invitations",
            params=None,
            json={"vehicle_id": vehicle_id},
        )

    def share_invites_revoke(self, vehicle_id, id):
        return self.httpPost(
            f"/api/1/vehicles/{vehicle_id}/invitations/{id}/revoke",
            params=None,
            json={"vehicle_id": vehicle_id, "id": id},
        )

    def signed_command(self, id, routable_message):
        return self.httpPost(
            f"/api/1/vehicles/{id}/signed_command",
            params=None,
            json={"id": id, "routable_message": routable_message},
        )

    def subscriptions(self, device_token: None, device_type: None):
        return self.httpGet(
            f"/api/1/subscriptions",
            params={"device_token": device_token, "device_type": device_type},
        )

    def subscriptions_set(self, device_token: None, device_type: None):
        return self.httpPost(
            f"/api/1/subscriptions",
            params={"device_token": device_token, "device_type": device_type},
            json=None,
        )

    def vehicle(self, id):
        return self.httpGet(
            f"/api/1/vehicles/{id}",
            params=None,
        )

    def vehicle_data(self, id, endpoints: None):
        return self.httpGet(
            f"/api/1/vehicles/{id}/vehicle_data",
            params={"endpoints": endpoints},
        )

    def vehicle_subscriptions(self, device_token: None, device_type: None):
        return self.httpGet(
            f"/api/1/vehicle_subscriptions",
            params={"device_token": device_token, "device_type": device_type},
        )

    def vehicle_subscriptions_set(self, device_token: None, device_type: None):
        return self.httpPost(
            f"/api/1/vehicle_subscriptions",
            params={"device_token": device_token, "device_type": device_type},
            json=None,
        )

    def wake_up(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/wake_up",
            params=None,
            json={"id": id},
        )

    def warranty_details(self, vin: None):
        return self.httpGet(
            f"/api/1/dx/warranty/details",
            params={"vin": vin},
        )
