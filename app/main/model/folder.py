"""
    Model for Folder names and its details
"""

from .base_model import Base
from .. import db
from sqlalchemy.dialects.mysql import TEXT


class Folder(Base):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('folder_name', db.String(255),
                     unique=True, nullable=False)
    path = db.Column('folder_path', TEXT)
