import os

from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader
from starlette import status

api_key_header = APIKeyHeader(name="x-api-key")
SYSTEM_API_KEY = os.getenv("SYSTEM_API_KEY")


def get_api_key(api_key_header: str = Security(api_key_header)) -> str:
    if api_key_header == SYSTEM_API_KEY:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )
