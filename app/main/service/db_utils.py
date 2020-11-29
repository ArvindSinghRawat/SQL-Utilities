"""
    Utilities related to Database
"""

from app.main import db


def save_changes(data):
    """Commit data in Database

    Args:
        data (DB Entity like User): Data to be saved in Database
    """
    db.session.add(data)
    db.session.commit()
