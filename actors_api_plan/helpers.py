import logging
from typing import Optional
import requests
import json

def setup_logger(name: Optional[str] = None):
    """Set up the logger."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(fmt="[%(asctime)s][%(name)s][%(levelname)s] %(message)s")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def get_type_service(service_id: str) -> str:
    response = requests.get(f"http://localhost:8080/services/{service_id}")
    actor = json.loads(response.text)
    return actor["attributes"]["type"]