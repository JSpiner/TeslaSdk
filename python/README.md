# Python TeslaSdk
[![PyPI version](https://badge.fury.io/py/teslasdk.svg)](https://badge.fury.io/py/teslasdk)

### Installation
```
$ pip3 install teslasdk
```

### Usage
Http api client
```python
from tesla_sdk.client.web.web_client import WebClient

client = WebClient("YOUR_AUTH_KEY")
vehicles = client.vehicles.list(1, 10)

print(vehicles)

# {'response': [{'id': 333333333333, 'vehicle_id': 333333333333, 'vin': '777777777777', 'color': None, 'access_type': 'OWNER', 'display_name': 'MyTesla', 'option_codes': None, 'granular_access': {'hide_private': False}, 'tokens': ['333333333333', '333333333333'], 'state': 'asleep', 'in_service': False, 'id_s': '333333333333', 'calendar_enabled': True, 'api_version': 63, 'backseat_token': None, 'backseat_token_updated_at': None, 'ble_autopair_enrolled': False}], 'count': 1}
```

### Api docs
- https://developer.tesla.com/docs/fleet-api

### Support
| Function | support  |
| -- | -- |
| Http base fleet API | ✅ full support |
| OAuth authenticate | will support | 
| ble api | no support |