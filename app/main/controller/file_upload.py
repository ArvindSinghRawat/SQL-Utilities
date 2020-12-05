# pylint:disable=R0201, R1710

"""
    Controller for Uploading files

Intentionally ignored:
    R0201: method could be a function... because of syntax
"""


from flask_restx import Resource
import werkzeug

from ..dto.upload_file_dto import UploadDto
from ..service.file_upload_service import upload_file, validate_file_extension
from ..util.common import create_response

api = UploadDto.api
_parser = UploadDto.upload_file_parser


@api.route("/")
class UploadCsvFile(Resource):
    """Used for File Upload related APIs"""
    @api.expect(_parser)
    @api.response(201, 'Successfully uploaded')
    @api.response(401, 'Requesting User not found')
    @api.response(403, 'File Extension not supported')
    def post(self):
        """Used to Upload files"""
        args = parser.parse_args()
        input_file = args["file"]
        file_name = args["file_name"]
        user_id = args["user_id"]
        if not validate_file_extension(input_file.filename):
            response_object = create_response(
                'fail', 'Extension of uploaded file is not supported')
            return response_object, 400

        upload_file(input_file, file_name, user_id)
