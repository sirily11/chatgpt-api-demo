from service.functions import BaseFunction


class GetWeather(BaseFunction):
    name = "weather"
    description = "Get the weather in a city"
    parameters = {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city to get the weather for",
            }
        },
    }

    def run(self, arguments: dict):
        print("Getting weather for", arguments["city"])

        return f"The weather in {arguments['city']} is 72 degrees and sunny"
