import logging
from whale.core.models.message import Message, Role
from whale.core.linear.client import LinearWhaleClient

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def main():
    linear_client = LinearWhaleClient(
        whale_api_key="your_whale_api_key", # Consider using environment variables
        integration_api_key="your_linear_api_key", # Consider using environment variables    
    )
    
    messages: list[Message] = [
        Message(
            role=Role.USER,
            content="I want to get all the issues assigned to Jin Yang" # Insert your message(s) here
        )
    ]
    
    response: dict = linear_client.query(messages=messages)
    log.info(response)
    return response 

if __name__ == "__main__":
    main()