import json
import logging
import os
from typing import List

import requests

from dto.message import Message
from service.api.api import ApiClient
from service.functions import BaseFunction
from service.functions.calculator import Calculator


class GPTService:
    def __init__(self):
        self.endpoint = "https://ai-helper.openai.azure.com/openai/deployments/chatbot/chat/completions?api-version=2023-07-01-preview"
        self.api_key = os.environ.get("OPENAI_API_KEY")

        api_client = ApiClient()
        api_client.run_function = self.run_function
        api_client.get_chat_response = self.run_conversation

        self.functions: List[BaseFunction] = [
            # Zoey(api=api_client),
            Calculator(api=api_client),
        ]
        self.history: list[Message] = []

    def run_conversation(self, message: str):
        # Step 1: send the conversation and available functions to the model
        messages = [{"role": "user", "content": message}]
        if len(self.history) > 0:
            # if there is a history, add it to the messages
            messages = self.history + messages
        function_call = [function.to_chatgpt_function_call_dict() for function in self.functions]

        # Step 2: send the messages and tools to the model
        response = requests.post(
            self.endpoint,
            headers={"api-key": self.api_key},
            json={"messages": messages, "functions": function_call, "function_call": "auto"},
        )

        if response.status_code != 200:
            logging.error(f"Error with status code {response.status_code} and message {response.json()}")
            return "Sorry, I don't know how to answer that."

        chatgpt_message = response.json()['choices'][0]['message']
        print(f"chatgpt_message: {messages}")
        if "function_call" in chatgpt_message:
            function_call = chatgpt_message['function_call']
            result = self.run_function(function_call['name'], function_call['arguments'])
        else:
            result = self.get_chat_response(chatgpt_message)

        # Step 3: Add the user's message and the assistant's response to the history
        self.history.append(Message(role="user", content=message))
        self.history.append(Message(role="assistant", content=result))

        return result

    def run_function(self, name: str, arguments: str):
        try:
            # {'role': 'assistant', 'function_call': {'name': 'weather', 'arguments': '{\n  "city": "San Francisco"\n}'}}
            arguments_dict = json.loads(arguments)
            for function in self.functions:
                if function.name == name:
                    return function.run(arguments_dict)
        except Exception as e:
            logging.error(f"Error running function {name} with arguments {arguments}: {e}")
            return "Sorry, I don't know how to answer that."

    def get_chat_response(self, chat_message) -> str:
        return chat_message['content']
