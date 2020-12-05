# pylint:disable=R0903

"""
    DTOs used in User related APIs
"""
from flask_restx import Namespace, fields

from ..util.regex import EMAIL_REGEX, PASSWORD_REGEX, UUID_REGEX


class UserDto:
    """
    DTO for User related API
    """
    api = Namespace("User",
                    description="User related operations")

    user_request = api.model("User Request", {
        "email": fields.String(required=True,
                               description="User e-mail",
                               pattern=EMAIL_REGEX),
        "username": fields.String(required=True, description="User name"),
        "password": fields.String(required=True,
                                  description="User password",
                                  min_length=8,
                                  pattern=PASSWORD_REGEX)
    })

    user_response = api.inherit("User Response", user_request, {
        "public_id": fields.String(description="User identifier",
                                   pattern=UUID_REGEX)
    })
