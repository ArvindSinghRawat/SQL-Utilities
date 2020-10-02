# pylint:disable=R0201, R1710

"""
Controller for User related operations
Exposes Endpoint for user interaction

Intentionally ignored:
    R0201: method could be a function... because of syntax
    R1710: Either all return statemen... because of explicit returns
"""

from flask import request
from flask_restx import Resource

from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    """Used for Users related API"""
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    """Used for single user related API"""
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """
        Get a user given its identifier

        Args:
            public_id (str): Public Id of the requested user

        Returns:
            User: Details of the requested User
        """
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user
