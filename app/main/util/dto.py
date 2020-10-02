"""
Module for DTOs used in project APIs
"""
from flask_restx import Namespace, fields


class UserDto:
    """
    DTO for User related API
    """
    api = Namespace('user', description='User related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='User e-mail'),
        'username': fields.String(required=True, description='User username'),
        'password': fields.String(required=True, description='User password'),
        'public_id': fields.String(description='User identifier')
    })
