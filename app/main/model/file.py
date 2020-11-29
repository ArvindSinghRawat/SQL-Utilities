"""
    Model for Files and related details
"""

from uuid import uuid4

from .base_model import Base
from .. import db

from .user import User
from .folder import Folder


class File(Base):
    id = db.Column('file_id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('file_name', db.String(255),
                     unique=True, nullable=False)
    masked_name = db.Column(db.String(100), unique=True,
                            default=uuid4(), nullable=False)

    # Relationships
    folder = db.Column('FK_folder_id', db.Integer,
                       db.ForeignKey('folder.folder_id'), nullable=False, unique=True)
    user = db.Column('FK_user_id', db.Integer,
                     db.ForeignKey('user.user_id'), nullable=False, unique=True)

    def __repr__(self):
        """Returns File's String Representation

        Returns:
            str: String Representation
        """
        return "<File '{}' at '{}'>".format(self.masked_name, self.folder)
