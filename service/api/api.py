class ApiClient:
    def get_chat_response(self, message: str) -> str:
        raise NotImplementedError()

    def run_function(self, name: str, arguments: str) -> str:
        raise NotImplementedError()