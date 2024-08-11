from pydantic import BaseModel

from whale.core.models.message import Message


class QueryRequest(BaseModel):
    messages: list[Message]
    whale_api_key: str
    integration_api_key: str
