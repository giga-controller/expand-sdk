from whale.core.models.message import Message
from pydantic import BaseModel

class QueryRequest(BaseModel):
    messages: list[Message]
    integration_api_key: str