import logging

import requests

from expand._utils._api_constants import LINEAR_ENDPOINT, SERVICE_URL
from expand._utils._request import QueryRequest
from expand.core._base import ExpandClient
from expand.core.models.message import Message

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class ExpandWhaleClient(ExpandClient):

    def query(self, messages: list[Message]) -> dict:
        try:
            log.info(f"Sending request to LinearWhaleClient")
            query_request = QueryRequest(
                messages=messages,
                whale_api_key=self.whale_api_key,
                integration_api_key=self.integration_api_key,
            )

            # ### FOR TESTING
            # SERVICE_URL = "http://0.0.0.0:8080"
            # ###
            response = requests.post(
                f"{SERVICE_URL}/{LINEAR_ENDPOINT}", json=query_request.model_dump()
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            log.error(f"Failed to infer response from LinearWhaleClient: {e}")
            raise e
        except Exception as e:
            log.error(f"Unknown error occured in LinearWhaleClient: {e}")
            raise e
