"""
    For Uploading files
"""


from flask import request
from flask_restx import Resource, Api, reqparse
import werkzeug

from ..util.dto import UploadDto

api = UploadDto.api

parser = api.parser()
parser.add_argument(
            "file", type=werkzeug.datastructures.FileStorage, location="files")
parser.add_argument(
            "file_name", type=str, location="form")

@api.route("/")
class UploadCsvFile(Resource):
    @api.expect(parser)
    def post(self):
        # parser = reqparse.RequestParser()
        # parser.add_argument(
        #     "file", type=werkzeug.datastructures.FileStorage, location="static")
        args = parser.parse_args()
        input_file = args["file"]
        file_name = args["file_name"]
        print("Input File length: " + str(input_file.content_length))
        print("Input File type: " + str(input_file.content_type))
        input_file.save(file_name)
