from pydantic import BaseModel
from whale.core._base import WhaleClient
import logging
from whale._utils._api_constants import LINEAR_ENDPOINT, SERVICE_URL
from whale.core.models.request import QueryRequest
import requests

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

class LinearWhaleClient(WhaleClient):
    
    def query(self, input: QueryRequest) -> dict:
        try:
            log.info(f"Sending request to LinearWhaleClient")
            response = requests.post(
                f"{SERVICE_URL}/{LINEAR_ENDPOINT}", json=input.model_dump()
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            log.error(f"Failed to infer response from LinearWhaleClient: {e}")
            raise e
        except Exception as e:
            log.error(f"Unknown error occured in LinearWhaleClient: {e}")
            raise e
