"""
    Business logic for File Upload related operations
"""
import os
from datetime import datetime
from werkzeug.datastructures import FileStorage
from sqlalchemy.exc import IntegrityError

from ..util.directory_traversal import create_nested_directories
from ..util import constants, common
from ..model.file import File
from ..model.folder import Folder
from ..model.user import User
from .db_utils import save_changes


def upload_file(file: FileStorage, file_name: str, public_id: str) -> tuple:
    """
    Method to Save a uploaded file in static folder

    Args:
        file (FileStorage): Uploaded File
        file_name (str): Desired name of the saved file, used to
        uniquely identify the file
    """
    user = User.query.filter(User.public_id == public_id).first()
    if user is None:
        return common.create_response("fail", "Requested User not Found"), 401
    target_dir = find_or_create_static_dir()
    try:
        save_and_upload_file(file_name=file_name, file=file,
                             folder=target_dir, user=user)
    except IntegrityError:
        return common.create_response("fail", f"'{file_name}' already exists"), 403
    return common.create_response("success", f"Successfully Uploaded '{file_name}' file"), 201


def find_or_create_static_dir() -> Folder:
    """
    Find or create static directory (if, not already exist) to store
    uploaded files

    Returns:
        Folder: Path to resultant directory
    """
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
    return found_folder


def find_folder(folder_name: str) -> Folder:
    """Find folder entry in Database

    Args:
        folder_name (str): Name of the actual folder

    Returns:
        Folder: DB Entry for the Found folder,
                None if doesn't exist
    """
    return Folder.query.filter(Folder.name == folder_name).first()


def save_and_upload_file(file_name: str, file: FileStorage,
                         folder: Folder, user: User):
    """Save the input file mapped to input filename

    Args:
        file_name (str): Name of the uploaded file
        file (FileStorage): Actual file to be stored
        folder (Folder): Folder object in which file is stored
        user (User): User uploading the file
    """
    new_file = File(name=file_name, folder=folder.id, user=user.id)
    save_changes(new_file)
    file.save(os.path.join(folder.path, new_file.masked_name))


def validate_file_extension(filename: str) -> bool:
    """Validates the extension of incoming file against allowed ones

    Args:
        filename (str): Name of the input file

    Returns:
        bool: True, if extension is allowed, otherwise false
    """
    try:
        return filename.rsplit('.', 1)[1] in constants.ALLOWED_FILE_TYPES
    except IndexError:
        return False
