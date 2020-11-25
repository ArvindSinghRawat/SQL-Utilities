"""
    For Uploading files
"""


from flask import request
from flask_restx import Resource, Api, reqparse
import werkzeug

from ..util.dto import UploadDto
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


@api.route("/")
class UploadCsvFile(Resource):
    @api.expect(parser)
    def post(self):
        args = parser.parse_args()
        input_file = args["file"]
        file_name = args["file_name"]
        upload_file(input_file, file_name)
