from fastapi import FastAPI

from service.gpt_service import GPTService

app = FastAPI()


@app.get("/")
async def root(query: str):
    service = GPTService()
    response = service.run_conversation(message=query)
    return {
        "message": response,
    }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
