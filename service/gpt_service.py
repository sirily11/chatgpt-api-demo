import json
import os
from typing import List

import requests

from service.functions import BaseFunction
from service.functions.calculator import Calculator
from service.functions.get_weather import GetWeather
from service.functions.zoey import Zoey


class GPTService:
    def __init__(self):
        self.endpoint = "https://ai-helper.openai.azure.com/openai/deployments/gpt4/chat/completions?api-version=2023-07-01-preview"
        self.api_key = os.environ.get("OPENAI_API_KEY")
        self.functions: List[BaseFunction] = [
            GetWeather(),
            Calculator(),
            Zoey(),
        ]

    def run_conversation(self, message: str):
        # Step 1: send the conversation and available functions to the model
        messages = [{"role": "user", "content": message}]
        function_call = [function.to_chatgpt_function_call_dict() for function in self.functions]

        # Step 2: send the messages and tools to the model
        response = requests.post(
            self.endpoint,
            headers={"api-key": self.api_key},
            json={"messages": messages, "functions": function_call, "function_call": "auto"},
        )

        chatgpt_message = response.json()['choices'][0]['message']
        if "function_call" in chatgpt_message:
            function_call = chatgpt_message['function_call']
            return self.run_function(function_call['name'], function_call['arguments'])
        else:
            return self.get_chat_response(chatgpt_message)

    def run_function(self, name: str, arguments: str):
        # {'role': 'assistant', 'function_call': {'name': 'weather', 'arguments': '{\n  "city": "San Francisco"\n}'}}
        arguments_dict = json.loads(arguments)
        for function in self.functions:
            if function.name == name:
                return function.run(arguments_dict)

    def get_chat_response(self, chat_message) -> str:
        return chat_message['content']
