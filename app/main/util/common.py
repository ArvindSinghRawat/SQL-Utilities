"""
Common utilities for the whole project
"""


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
