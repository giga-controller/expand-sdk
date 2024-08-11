from whale.core.models.message import Message
from pydantic import BaseModel

class QueryRequest(BaseModel):
    messages: list[Message]
    whale_api_key: str
    integration_api_key: str