from service.functions import BaseFunction


class Zoey(BaseFunction):
    name = "Zoey"
    description = "Get info about Zoey"
    parameters = {
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": "The question to ask Zoey",
            }
        },
    }

    def run(self, arguments: dict):
        question = arguments["question"]

        return f"Asked zoey: {question}"
