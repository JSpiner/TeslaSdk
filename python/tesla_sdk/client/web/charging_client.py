from tesla_sdk.client.web.base_web_client import BaseWebClient


class ChargingClient(BaseWebClient):

    def charging_history(self, vin: None, startTime: None, endTime: None, pageNo: None, pageSize: None, sortBy: None, sortOrder: None):
        return self.httpGet(
            f"/api/1/dx/charging/history",
            params={"vin": vin, "startTime": startTime, "endTime": endTime, "pageNo": pageNo,
                    "pageSize": pageSize, "sortBy": sortBy, "sortOrder": sortOrder},
        )

    def charging_sessions__only_for_business_fleet_owners_(self, vin: None, date_from: None, date_to: None, limit: None, offset: None):
        return self.httpGet(
            f"/api/1/dx/charging/sessions",
            params={"vin": vin, "date_from": date_from,
                    "date_to": date_to, "limit": limit, "offset": offset},
        )
