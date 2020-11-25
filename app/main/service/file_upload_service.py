"""
    Business logic for File Upload related operations
"""
from werkzeug.datastructures import FileStorage

def upload_file(file: FileStorage, file_name: str):
    """
    Method to Save a uploaded file in user folder 

    Args:
        file (FileStorage): Uploaded File
        file_name (str): Desired name of the saved file, used to uniquely identify the file
    """
    file.save(file_name)
