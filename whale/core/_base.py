import logging
from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel

from whale.core.models.message import Message

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class WhaleClient(BaseModel, ABC):
    whale_api_key: str
    integration_api_key: str

    @abstractmethod
    def query(self, messages: list[Message]) -> Any:
        pass
