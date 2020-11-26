"""
    DTOs used in User related APIs
"""
from flask_restx import Namespace, fields

from ..util.regex import EMAIL_REGEX, PASSWORD_REGEX, UUID_REGEX


class UserDto:
    """
    DTO for User related API
    """
    api = Namespace("user",
                    description="User related operations")
    user_input = api.model("user_input", {
        "email": fields.String(required=True,
                               description="User e-mail",
                               pattern=EMAIL_REGEX),
        "username": fields.String(required=True, description="User name"),
        "password": fields.String(required=True,
                                  description="User password",
                                  min_length=8,
                                  pattern=PASSWORD_REGEX)
    })
    user = api.inherit("user", user_input, {
        "public_id": fields.String(description="User identifier",
                                   pattern=UUID_REGEX)
    })
