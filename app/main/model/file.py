"""
    Model for Files and related details
"""

from .base_model import Base
from .. import db
from ..util.common import create_random_uuid

from .user import User
from .folder import Folder


class File(Base):
    id = db.Column('file_id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('file_name', db.String(255),
                     unique=True, nullable=False)
    masked_name = db.Column(db.String(100), unique=True,
                            default=create_random_uuid, nullable=False)

    # Relationships
    folder = db.Column('folder_id', db.Integer,
                       db.ForeignKey('folder.folder_id'), nullable=False)
    user = db.Column('user_id', db.Integer,
                     db.ForeignKey('user.user_id'), nullable=False)

    users = db.relationship(User)
    folders = db.relationship(Folder)

    def __repr__(self):
        """Returns File's String Representation

        Returns:
            str: String Representation
        """
        return "<File '{}' at '{}'>".format(self.masked_name, self.folder)
