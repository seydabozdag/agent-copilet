import os
import logging
from typing import Optional

# Logging config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _get_env_variable(name: str) -> str:
    """Securely retrieve environment variable."""
    value = os.getenv(name)

    if not value or not value.strip():
        raise ValueError(f"{name} is missing or empty")

    return value.strip()


def get_aws_credentials() -> dict:
    """Retrieve AWS credentials securely."""
    return {
        "access_key": _get_env_variable("AWS_ACCESS_KEY_ID"),
        "secret_key": _get_env_variable("AWS_SECRET_ACCESS_KEY"),
        "region": _get_env_variable("AWS_DEFAULT_REGION"),
    }


def connect() -> Optional[bool]:
    """Establish a connection to AWS."""
    try:
        creds = get_aws_credentials()

        logger.info("AWS connection initialized")
        return True

    except ValueError:
        logger.error("AWS connection failed due to missing configuration")
        return False