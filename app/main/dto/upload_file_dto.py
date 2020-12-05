# pylint:disable=R0903

"""
    DTO for APIs related to Upload Files
"""
import werkzeug
from flask_restx import Namespace


class UploadDto:
    """
    DTO for Upload related API
    """
    api = Namespace("Upload Files",
                    description="Upload related operations")

    upload_file_parser = api.parser()
    upload_file_parser.add_argument(
        "file", required=True, location="files",
        type=werkzeug.datastructures.FileStorage)
    upload_file_parser.add_argument(
        "file_name", required=True, location="form", type=str)
    upload_file_parser.add_argument(
        "user_id", required=True, location="form", type=str)

