from fastapi import FastAPI, Security

from dto.query import ChatQueryDto
from security import get_api_key
from service.gpt_service import GPTService

app = FastAPI()
service = GPTService()


@app.post("/chat")
async def chat(query: ChatQueryDto, api_key: str = Security(get_api_key)):
    response = service.run_conversation(message=query.query)
    return {
        "message": response,
        "id": query.id,
    }
