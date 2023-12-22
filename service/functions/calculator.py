from service.functions import BaseFunction


class Calculator(BaseFunction):
    name = "calculator"
    description = "你是一个计算机，负责帮助用户进行计算。如果用户问到任何需要进行计算的事情，就来找你！为了进行计算，你需要用户提供两个数字作为输入。"
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
        "required": ["number1", "number2"],
    }

    def run(self, arguments: dict):
        print("Calculating", arguments["number1"], arguments["number2"])
        number1 = arguments["number1"]
        number2 = arguments["number2"]

        return f"{number1} + {number2} = {number1 + number2}"