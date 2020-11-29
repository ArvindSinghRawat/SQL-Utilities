# pylint:disable=R0201, R1710

"""
    Controller for Uploading files

Intentionally ignored:
    R0201: method could be a function... because of syntax
"""


from flask_restx import Resource
import werkzeug

from ..dto.upload_file_dto import UploadDto
from ..service.file_upload_service import upload_file

api = UploadDto.api

parser = api.parser()
parser.add_argument(
    "file",
    type=werkzeug.datastructures.FileStorage,
    location="files")
parser.add_argument(
    "file_name",
    type=str,
    location="form")
parser.add_argument(
    "user_id",
    type=str,
    location="form"
)


@api.route("/")
class UploadCsvFile(Resource):
    """Used for File Upload related APIs"""
    @api.expect(parser)
    def post(self):
        """Used to Upload files"""
        args = parser.parse_args()
        input_file = args["file"]
        file_name = args["file_name"]
        user_id = args["user_id"]
        upload_file(input_file, file_name, user_id)
