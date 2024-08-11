from whale.core._base import WhaleClient
from whale.core.models.message import Message

class LinearWhaleClient(WhaleClient):
    def query(self, messages: list[Message]) -> BaseModel:
        pass
