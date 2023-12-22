from pydantic import BaseModel

from dto.message import Message


class ChatSession(BaseModel):
    id: str
    settings_message: list[Message]