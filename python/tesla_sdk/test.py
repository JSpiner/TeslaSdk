from client.web.web_client import WebClient
import json

with open("test_key.json", "r") as st_json:
    keyJson = json.load(st_json)

    client = WebClient(keyJson['auth_token'])
    response = client.vehicles.list(1, 10)

    print(response.status_code)
    print(response.text)