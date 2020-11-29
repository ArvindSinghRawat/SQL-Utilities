"""
    User Model for different Users
"""

from uuid import uuid4

from .. import db, flask_bcrypt
from .base_model import Base


class User(Base):
    """ User Model for storing user related details """
    __tablename__ = "user"

    id = db.Column('user_id', db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column('is_admin', db.Boolean, nullable=False, default=False)
    public_id = db.Column(db.String(100), unique=True,
                          default=uuid4, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    
    # Relationships
    files = db.relationship('File', backref='creator', lazy=True)

    @property
    def password(self):
        """Throws error on Read Access

        Raises:
            AttributeError: Password is a Write Only Field
        """
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        """Sets Password using Hash

        Args:
            password (str): Entered password
        """
        self.password_hash = flask_bcrypt.generate_password_hash(
            password).decode('utf-8')

    def check_password(self, password: str) -> bool:
        """Validates password for a User

        Args:
            password (str): Entered Password

        Returns:
            bool: Entered password matches stored password or not
        """
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        """Returns User's String Representation

        Returns:
            str: String Representation
        """
        return "<User '{}'>".format(self.username)
