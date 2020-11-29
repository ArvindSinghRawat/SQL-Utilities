"""
Common utilities for the whole project
"""

from uuid import uuid4


def create_response(status: str, message: str) -> dict:
    """
    Creates a response object

    Args:
        status (str): Status of the API/Method Called
        message (str): Human Friendly message for the Response

    Returns:
        dict: Response Object with status and message
    """
    return {
        'status': status,
        'message': message
    }


def create_random_uuid() -> str:
    return str(uuid4())
