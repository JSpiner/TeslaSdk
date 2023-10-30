# Python TeslaSdk

### Installation
This project has not yet been deployed.

### Usage
Http api client
```python
from tesla_sdk.client.web.web_client import WebClient

client = WebClient("YOUR_AUTH_KEY")
response = client.vehicles.list(1, 10)

print(response.status_code)
print(response.text)
```

### Api docs
- https://developer.tesla.com/docs/fleet-api