from pydantic import BaseModel


class AuctionSettings(BaseModel):
    model: str
    