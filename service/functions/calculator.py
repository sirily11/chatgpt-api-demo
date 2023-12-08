from service.functions import BaseFunction


class Calculator(BaseFunction):
    name = "calculator"
    description = "Calculate a math for given two numbers"
    parameters = {
        "type": "object",
        "properties": {
            "number1": {
                "type": "number",
                "description": "The first number",
            },
            "number2": {
                "type": "number",
                "description": "The second number",
            },
        },
    }

    def run(self, arguments: dict):
        print("Calculating", arguments["number1"], arguments["number2"])
        number1 = arguments["number1"]
        number2 = arguments["number2"]

        return f"{number1} + {number2} = {number1 + number2}"