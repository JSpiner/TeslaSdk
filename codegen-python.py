import json
import re

with open("api-spec.json", "r") as file:
    apiSpec = json.load(file)

    targetSection = "Charging Endpoints"

    for name in apiSpec[targetSection]:
        function = apiSpec[targetSection][name]
        
        functionName = name.replace(" ", "_").replace("(", "_").replace(")", "_")
        endpoint = function['endpoint']
        parameters = function['parameters'] if 'parameters' in function else []

        if endpoint.startswith('GET'):
            method = 'GET'
            url = endpoint[4:]
        else:
            method = 'POST'
            url = endpoint[5:]

        # print(function)
        # print(name)
        # print(endpoint)
        # print(method)
        # print(url)
        # print(parameters)
        parametersInFunction = ", ".join(
            list(
                map(
                    lambda parameter: parameter['name'] if parameter['required'] == "Yes" else parameter['name'] + ": None",
                    parameters
                )
            )
        )
        queryParameters = ", ".join(
            list(
                map(
                    lambda parameter: f"\"{parameter['name']}\": {parameter['name']}",
                    filter(
                        lambda parameter: parameter['in'] == "query",
                        parameters
                    )
                )
            )
        )
        bodyParameters = ", ".join(
            list(
                map(
                    lambda parameter: f"\"{parameter['name']}\": {parameter['name']}",
                    filter(
                        lambda parameter: parameter['in'] != "query",
                        parameters
                    )
                )
            )
        )

        if method == 'GET':
            functionString = f"""
def {functionName}(self, {parametersInFunction}):
    return self.httpGet(
        f"{url}",
        params={"None" if len(queryParameters) == 0 else "{" + queryParameters + "}"},
    )
            """
        else:
            functionString = f"""
def {functionName}(self, {parametersInFunction}):
    return self.httpPost(
        f"{url}",
        params={"None" if len(queryParameters) == 0 else "{" + queryParameters + "}"},
        json={"None" if len(bodyParameters) == 0 else "{" + bodyParameters + "}"},
    )
            """
        print(functionString)
