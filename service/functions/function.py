class BaseFunction:
    name: str
    description: str
    parameters: dict

    def run(self, arguments: dict):
        """
        Run function with given arguments
        :param arguments:
        :return:
        """
        raise NotImplementedError()

    def to_chatgpt_function_call_dict(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters,
        }
