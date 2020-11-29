"""
Business logic for Users related operations
"""
import uuid
import datetime

from app.main.model.user import User

from ..util.common import create_response
from .db_utils import save_changes


def save_new_user(data: dict) -> dict:
    """
    Creates a new User in DB, if not already present
    If email is already present, returns Fail message

    Args:
        data (dict): Details of the new user

    Returns:
        dict: Dictionary of Success or Failure response
    """
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response_object = create_response(
            'success', 'Successfully registered.')
        return response_object, 201
    response_object = create_response(
        'fail', 'User already exists. Please Log in.')
    return response_object, 409


def get_all_users():
    """Return all the users from DB

    Returns:
        List: List of all avialable users
    """
    return User.query.all()


def get_a_user(public_id: str) -> User:
    """Finds a user by Public Id of the user

    Args:
        public_id (str): Public UUID of the user

    Returns:
        User: User if found, otherwise None
    """
    return User.query.filter_by(public_id=public_id).first()
