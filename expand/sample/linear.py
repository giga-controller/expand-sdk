import logging

from expand.core.linear.client import ExpandWhaleClient
from expand.core.models.message import Message, Role
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def main():
    linear_client = ExpandWhaleClient(
        # whale_api_key="your_whale_api_key", 
        whale_api_key=os.getenv("WHALE_API_KEY"), # Consider using environment variables
        # integration_api_key="your_linear_api_key",  
        integration_api_key=os.getenv("LINEAR_API_KEY") # Consider using environment variables
    )

    messages: list[Message] = [
        Message(
            role=Role.USER,
            content="I want to get all the issues that are assigned to cycle 1",  # Insert your message(s) here
        )
    ]

    response: list[dict] = linear_client.query(messages=messages)
    log.info(response)
    return response


if __name__ == "__main__":
    main()
