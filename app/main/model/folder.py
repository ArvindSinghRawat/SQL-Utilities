# pylint:disable=E1101, R0903

"""
    Model for Folder names and its details
"""

from sqlalchemy.dialects.mysql import TEXT
from .base_model import Base
from .. import db


class Folder(Base):
    """Model for storing folder related details

    Args:
        Base (Abstract Model): Abstract base class for all models
    """
    id = db.Column('folder_id', db.Integer,
                   primary_key=True, autoincrement=True)
    name = db.Column('folder_name', db.String(255),
                     unique=True, nullable=False)
    path = db.Column('folder_path', TEXT, nullable=False)
    for_date = db.Column(db.Date, default=db.func.now(), nullable=False)

    # Relationships
    files = db.relationship('File', backref='container_folder', lazy=True)

    def __repr__(self):
        """Returns Folder's String Representation

        Returns:
            str: String Representation
        """
        return "<Folder '{}'>".format(self.name)
