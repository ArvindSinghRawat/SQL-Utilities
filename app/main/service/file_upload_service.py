"""
    Business logic for File Upload related operations
"""
import os
from datetime import datetime
from werkzeug.datastructures import FileStorage
from time import strftime

from ..util.directory_traversal import create_nested_directories
from ..util import constants
from ..model.file import File
from ..model.folder import Folder
from ..model.user import User
from .db_utils import save_changes


def upload_file(file: FileStorage, file_name: str, public_id: str):
    """
    Method to Save a uploaded file in user folder 

    Args:
        file (FileStorage): Uploaded File
        file_name (str): Desired name of the saved file, used to uniquely identify the file
    """
    target_dir = find_or_create_static_dir()
    user = User.query.filter(public_id == public_id).first()
    save_and_upload_file(file_name=file_name, file=file, folder=target_dir, user=user)


def find_or_create_static_dir() -> Folder:
    source_path = constants.USER_DIRECTORY
    current_date = datetime.now()
    parent_dir = current_date.strftime(constants.DIR_FORMAT)
    found_folder = find_folder(parent_dir)
    if found_folder is None:
        source_path = os.path.join(source_path, parent_dir)
        target = create_nested_directories("./", source_path.split('/'))
        new_folder = Folder(name=parent_dir, path=target)
        save_changes(new_folder)
        return new_folder
    else:
        return found_folder


def find_folder(folder_name: str) -> Folder:
    return Folder.query.filter(Folder.name == folder_name).first()


def save_and_upload_file(file_name: str, file: FileStorage, folder: Folder, user: User):
    new_file = File(name=file_name, folder=folder.id, user=user.id)
    save_changes(new_file)
    file.save(os.path.join(folder.path, new_file.masked_name))
