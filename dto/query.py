from pydantic import BaseModel


class ChatQueryDto(BaseModel):
    id: str
    query: str
