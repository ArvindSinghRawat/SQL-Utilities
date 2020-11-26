"""
    Base Model Class for all the ther models
"""

from .. import db


class Base(db.Model):
    __abstract__ = True

    created_on = db.Column(db.DateTime, default=db.func.now())
    created_by = db.Column(db.String(255), default='APP')
    modified_on = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now())
    modified_by = db.Column(db.String(255), default='APP', onupdate='APP')
    deleted = db.Column(db.Boolean, default=False)
