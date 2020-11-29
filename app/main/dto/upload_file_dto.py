# pylint:disable=R0903

"""
    DTO for APIs related to Upload Files
"""

from flask_restx import Namespace


class UploadDto:
    """
    DTO for Upload related API
    """
    api = Namespace("upload",
                    description="Upload related operations")
